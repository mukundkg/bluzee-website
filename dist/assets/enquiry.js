'use strict';
(() => {
  const form = document.querySelector('[data-enquiry-config]');
  if (!form) return;
  const config = JSON.parse(form.dataset.enquiryConfig);
  const field = name => form.elements.namedItem(name);
  const select = field('offering');
  const fields = form.querySelector('.enquiry-fields');
  const submit = form.querySelector('.enquiry-submit');
  const status = form.querySelector('.enquiry-status');
  const recovery = form.querySelector('.enquiry-recovery');
  const verify = form.querySelector('.enquiry-verify');
  const another = form.querySelector('.enquiry-another');
  const copyStatus = form.querySelector('.enquiry-copy-status');
  const normalise = value => String(value || '').replaceAll('™', '').trim();
  const route = () => config.ai_offerings.some(name => normalise(name) === normalise(select.value)) ? config.ai : config.general;
  const selected = normalise(new URLSearchParams(location.search).get('offering'));
  const option = [...select.options].find(item => normalise(item.value) === selected);
  if (option) select.value = option.value;
  let busy = false;
  let sent = false;
  let nativeVerification = false;
  const show = (state, message, focus = true) => {
    status.dataset.state = state;
    status.textContent = message;
    status.hidden = false;
    if (focus) status.focus();
  };
  const updateRoute = () => {
    const target = route();
    form.action = target.endpoint;
    const note = form.querySelector('.recipient-note');
    note.textContent = (target === config.ai ? 'AI product enquiries: ' : 'General enquiries: ') + target.recipient;
    form.querySelector('.enquiry-email').href = 'mailto:' + target.recipient;
  };
  select.addEventListener('change', updateRoute);
  for (const name of ['name', 'email', 'message']) {
    field(name).addEventListener('input', () => field(name).setCustomValidity(''));
  }
  const valid = () => {
    for (const name of ['name', 'email', 'message']) {
      const input = field(name);
      input.value = input.value.trim();
      input.setCustomValidity(input.value ? '' : 'Please complete this field.');
    }
    return form.reportValidity();
  };
  const pending = on => {
    busy = on;
    fields.disabled = on;
    submit.disabled = on;
    form.setAttribute('aria-busy', String(on));
    submit.textContent = on ? 'Sending…' : 'Send enquiry ↗';
  };
  form.addEventListener('submit', async event => {
    if (nativeVerification) return;
    event.preventDefault();
    if (busy || sent || !valid()) return;
    updateRoute();
    const data = new FormData(form);
    for (const name of ['name', 'email', 'organisation', 'message']) data.set(name, String(data.get(name) || '').trim());
    data.set('subject', 'Bluzee website enquiry: ' + select.value);
    data.set('source', 'Bluzee website contact form');
    data.set('privacy_notice', 'Website enquiry privacy notice — 2026-10-25');
    recovery.hidden = true;
    verify.hidden = true;
    copyStatus.textContent = '';
    pending(true);
    show('pending', 'Sending your enquiry…', false);
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 25000);
    try {
      const response = await fetch(form.action, {
        method: 'POST', body: data, headers: {Accept: 'application/json'},
        credentials: 'omit', signal: controller.signal
      });
      const result = await response.json().catch(() => null);
      if (response.ok && result?.ok === true) {
        sent = true;
        fields.hidden = true;
        submit.hidden = true;
        another.hidden = false;
        show('success', 'Thank you. Your enquiry has been submitted to Bluzee. We’ll respond using the email address you provided.');
      } else {
        const errors = JSON.stringify(result?.errors || result?.error || '').toLowerCase();
        const captcha = /captcha|challenge|verification/.test(errors);
        recovery.hidden = false;
        verify.hidden = !(captcha || (response.ok && result?.ok !== true));
        let message;
        if (!verify.hidden) message = 'An additional security check is needed. Continue with secure verification to finish submitting through Formspree. Your details are retained below.';
        else if (response.status === 429) message = 'The enquiry service is temporarily limiting submissions. Your details are retained. Please try later, email Bluzee or use WhatsApp.';
        else if (response.status >= 400 && response.status < 500) message = 'The enquiry service did not accept this submission. Please check your details and try again, or use email or WhatsApp. Your details are retained.';
        else message = 'We couldn’t confirm your submission. Your details are retained. You can retry or contact Bluzee by email or WhatsApp; retrying may create a duplicate.';
        show('error', message);
      }
    } catch (_) {
      recovery.hidden = false;
      show('error', 'We couldn’t confirm your submission because the connection was interrupted or timed out. Your details are retained. You can retry or use email or WhatsApp; retrying may create a duplicate.');
    } finally {
      clearTimeout(timer);
      pending(false);
    }
  });
  verify.addEventListener('click', () => {
    if (busy || sent || !valid()) return;
    updateRoute();
    nativeVerification = true;
    // A deliberate visitor action opens Formspree's normal POST/security flow.
    HTMLFormElement.prototype.submit.call(form);
  });
  form.querySelector('.enquiry-copy').addEventListener('click', async () => {
    const text = `Hello Bluzee,\n\nI would like to discuss ${select.value}.\n\n${field('message').value}\n\nName: ${field('name').value}\nEmail: ${field('email').value}\nOrganisation: ${field('organisation').value || 'Not specified'}`;
    try { await navigator.clipboard.writeText(text); copyStatus.textContent = 'Message copied. Paste it into your email or WhatsApp conversation.'; }
    catch (_) { copyStatus.textContent = 'Copying is unavailable. Please select and copy the text from the form fields.'; }
  });
  another.addEventListener('click', () => {
    form.reset();
    sent = false;
    fields.hidden = false;
    submit.hidden = false;
    another.hidden = true;
    status.hidden = true;
    recovery.hidden = true;
    updateRoute();
    field('name').focus();
  });
  updateRoute();
  submit.disabled = false;
})();
