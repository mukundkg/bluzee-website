// Offline integration tests: no HTTP requests or notification emails are sent.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const root = __dirname;
const html = fs.readFileSync(path.join(root, 'dist/contact/index.html'), 'utf8');
const script = fs.readFileSync(path.join(root, 'dist/assets/enquiry.js'), 'utf8');
const decode = s => s.replaceAll('&quot;', '"').replaceAll('&amp;', '&').replaceAll('&#x27;', "'");
const config = JSON.parse(decode(html.match(/data-enquiry-config="([^"]+)"/)[1]));
const options = [...html.matchAll(/<option(?: value="([^"]*)")?>([^<]*)<\/option>/g)].map(x => ({value:decode(x[1] ?? x[2])}));
assert.equal(config.general.endpoint, 'https://formspree.io/f/mbgggrko');
assert.equal(config.ai.endpoint, 'https://formspree.io/f/mjyyyboo');
assert(!html.includes('Nothing is sent from this concept'));
assert(html.includes('../enquiry-privacy/index.html'));

function fixture({query='', response={ok:true,status:200,body:{ok:true}}, reject=false, hold=false}={}) {
  class Element {
    constructor(value='') { this.value=value;this.handlers={};this.hidden=false;this.disabled=false;this.dataset={};this.checked=true;this.textContent='';this.custom=''; }
    addEventListener(type, fn) {this.handlers[type]=fn;}
    async emit(type) {return this.handlers[type]?.({preventDefault(){}});}
    setCustomValidity(value){this.custom=value;}
    setAttribute(name,value){this[name]=value;}
    focus(){this.focused=true;}
  }
  const fields={name:new Element(' Visitor '),email:new Element(' visitor@example.com '),organisation:new Element(' Example '),offering:new Element('General enquiry'),message:new Element(' A test enquiry '),enquiry_consent:new Element('agreed')};
  fields.offering.options=options;
  const nodes={};
  const form=new Element();
  form.dataset.enquiryConfig=JSON.stringify(config);
  form.action=config.general.endpoint;
  form.elements={namedItem:name=>fields[name]};
  form.querySelector=q=>nodes[q] ||= new Element();
  form.reportValidity=()=>['name','email','message'].every(k=>fields[k].value.trim()&&!fields[k].custom)&&!!fields.offering.value&&fields.enquiry_consent.checked;
  form.reset=()=>{for(const f of Object.values(fields))f.value='';fields.enquiry_consent.checked=false;};
  class FormData {
    constructor(){this.values=new Map(Object.entries(fields).map(([k,v])=>[k,v.value]));}
    get(k){return this.values.get(k);}
    set(k,v){this.values.set(k,v);}
  }
  const calls=[];let release;let timer;let nativeCount=0;
  const context={document:{querySelector:()=>form},location:{search:query},URLSearchParams,FormData,AbortController,
    navigator:{clipboard:{writeText:async()=>{}}},HTMLFormElement:{prototype:{submit(){nativeCount++;}}},
    setTimeout(fn){timer=fn;return 1;},clearTimeout(){},
    fetch:async(url,opts)=>{calls.push({url,data:Object.fromEntries(opts.body.values),opts});
      if(hold) await new Promise((resolve,reject)=>{release=resolve;opts.signal.addEventListener('abort',()=>reject(new Error('aborted')));});
      if(reject)throw Error('network');
      return {ok:response.ok,status:response.status,json:async()=>{if(response.badJSON)throw Error('invalid JSON');return response.body;}};
    }
  };
  vm.runInNewContext(script,context);
  return {form,fields,nodes,calls,submit:()=>form.emit('submit'),release:()=>release(),timeout:()=>timer(),native:()=>nativeCount};
}
(async()=>{
  let count=0;
  for(const option of options.filter(o=>o.value)) {
    const f=fixture();f.fields.offering.value=option.value;await f.fields.offering.emit('change');
    assert.equal(f.form.action,/DealTailor|Dimaq/.test(option.value)?config.ai.endpoint:config.general.endpoint);count++;
  }
  const pre=fixture({query:'?offering=Bluzee%20Dimaq'});assert.equal(pre.form.action,config.ai.endpoint);count++;
  for (const invalid of ['name','email','message']) {const f=fixture();f.fields.offering.value='General enquiry';f.fields[invalid].value='   ';await f.submit();assert.equal(f.calls.length,0);count++;}
  const consent=fixture();consent.fields.offering.value='General enquiry';consent.fields.enquiry_consent.checked=false;await consent.submit();assert.equal(consent.calls.length,0);count++;
  for (const offering of ['Bluzee DealTailor™','General enquiry']) {
    const f=fixture();f.fields.offering.value=offering;await f.submit();
    assert.equal(f.calls.length,1);assert.equal(f.calls[0].url,offering.includes('DealTailor')?config.ai.endpoint:config.general.endpoint);
    assert.equal(f.calls[0].data.email,'visitor@example.com');assert.equal(f.calls[0].data.name,'Visitor');assert.equal(f.calls[0].data.enquiry_consent,'agreed');
    assert.equal(f.nodes['.enquiry-status'].dataset.state,'success');assert(f.nodes['.enquiry-fields'].hidden);assert(!f.nodes['.enquiry-another'].hidden);
    await f.submit();assert.equal(f.calls.length,1);await f.nodes['.enquiry-another'].emit('click');assert(!f.nodes['.enquiry-fields'].hidden);assert.equal(f.fields.message.value,'');count++;
  }
  for(const response of [
    {ok:false,status:400,body:{errors:[{message:'Invalid email'}]}},
    {ok:false,status:429,body:{error:'rate limit'}},
    {ok:false,status:503,body:{error:'unavailable'}},
    {ok:true,status:200,badJSON:true},
    {ok:true,status:200,body:{ok:false}}
  ]) {const f=fixture({response});f.fields.offering.value='General enquiry';await f.submit();assert.equal(f.nodes['.enquiry-status'].dataset.state,'error');assert.equal(f.fields.message.value,'A test enquiry');assert(!f.nodes['.enquiry-fields'].disabled);assert.equal(f.native(),0);count++;}
  const captcha=fixture({response:{ok:false,status:400,body:{errors:[{code:'CAPTCHA_FAILED'}]}}});captcha.fields.offering.value='Bluzee Dimaq™';await captcha.submit();assert(!captcha.nodes['.enquiry-verify'].hidden);assert.equal(captcha.native(),0);await captcha.nodes['.enquiry-verify'].emit('click');assert.equal(captcha.native(),1);assert.equal(captcha.form.action,config.ai.endpoint);count++;
  const offline=fixture({reject:true});offline.fields.offering.value='General enquiry';await offline.submit();assert.equal(offline.nodes['.enquiry-status'].dataset.state,'error');assert(offline.nodes['.enquiry-status'].textContent.includes('couldn’t confirm'));count++;
  const pending=fixture({hold:true});pending.fields.offering.value='General enquiry';const first=pending.submit();await pending.submit();assert.equal(pending.calls.length,1);assert(pending.nodes['.enquiry-submit'].disabled);pending.release();await first;assert.equal(pending.nodes['.enquiry-status'].dataset.state,'success');count++;
  const timeout=fixture({hold:true});timeout.fields.offering.value='General enquiry';const waiting=timeout.submit();timeout.timeout();await waiting;assert.equal(timeout.nodes['.enquiry-status'].dataset.state,'error');assert.equal(timeout.fields.message.value,'A test enquiry');assert(!timeout.nodes['.enquiry-submit'].disabled);count++;
  console.log(JSON.stringify({checks:count,result:'passed',live_submissions_sent:0}));
})().catch(err=>{console.error(err);process.exitCode=1;});
