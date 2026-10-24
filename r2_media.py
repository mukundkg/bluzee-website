"""R2 media configuration for the Cloudflare Pages preview.

Original provenance remains in content-source/preservation-inventory.json.
Only exact names from the user's media inventory are used.
"""
from pathlib import Path
from html import escape
from urllib.parse import quote
import json
import re

ROOT = Path(__file__).parent
CONFIG = json.loads((ROOT / 'content-source/r2-media.json').read_text(encoding='utf-8'))


def media_url(key):
    return CONFIG['media_base_url'].rstrip('/') + '/' + quote(key, safe='/')


def configure(proof):
    proof['adheena'] = {
        'id': 'adheena', 'title': 'Adheena',
        'original_player_url': '', 'source_pages': ['https://www.bluzee.xyz/experiencehub'],
        'media_note': 'Name and testimonial classification supplied by owner; no quotation added.'
    }
    proof['barry-interview'] = {
        'id': 'barry-interview', 'title': 'Barry in conversation with Adri',
        'source_pages': ['https://www.bluzee.xyz/'],
        'media_note': 'Title follows owner-supplied filename. No event date or venue inferred.'
    }
    for key, object_key in CONFIG['videos'].items():
        item = proof[key]
        item['legacy_video_url'] = item.get('original_video_url')
        item['legacy_player_url'] = item.get('original_player_url')
        item['original_video_url'] = media_url(object_key)
        item['r2_object_key'] = object_key
        if 'original_player_url' in item:
            item['original_player_url'] = item['original_video_url']


def poster(key, title, u):
    if key == 'adheena':
        return '<div class="participant-placeholder" aria-hidden="true"><span class="participant-initial">A</span><span class="participant-name">Adheena</span><span class="participant-caption">PARTICIPANT PERSPECTIVE</span></div>'
    asset = 'assets/leadership/barry-fourie.webp' if key == 'barry-interview' else 'assets/proof-' + key + '.webp'
    alt = 'Barry Fourie, Bluzee advisor' if key == 'barry-interview' else title
    return f'<img src="{u(asset)}" alt="{escape(alt)}" loading="lazy" decoding="async">'


def transform_html(html, page, u):
    # Gallery previews already live in dist/assets and remain small and responsive.
    # Full-size links use R2 when the original was matched; otherwise the local
    # preserved copy is used, never a guessed or different image.
    for asset, entry in CONFIG['gallery'].items():
        target = media_url(entry['r2_key']) if entry['r2_key'] else u(asset)
        html = html.replace('href="' + entry['original_url'] + '"', 'href="' + escape(target) + '"')
    for asset, key in CONFIG['logos'].items():
        # Keep small local logo files for rendering; record the cloud original.
        html = html.replace('src="' + u(asset) + '"', 'src="' + u(asset) + '" data-original-src="' + escape(media_url(key)) + '"')
    for filename, key in CONFIG['portraits'].items():
        original = u('assets/leadership/' + filename)
        small = u('assets/leadership/' + Path(filename).stem + '.webp')
        html = html.replace('src="' + original + '"', 'src="' + small + '" data-original-src="' + escape(media_url(key)) + '"')
    html = html.replace('href="' + u('assets/volvo-feedback-original.png') + '"', 'href="' + escape(media_url(CONFIG['appreciation'])) + '"')
    html = html.replace('Original participant videos open in Bluzee’s existing video gallery.', 'Watch participants share their experience, in their own words.')
    html = html.replace('Student recordings open in Bluzee’s original Wix gallery.', 'Participant recordings play here with their original audio and video.')
    # Point original-gallery navigation to the preserved collections.
    for old, target, old_label, label in [
        ('https://www.bluzee.xyz/workshop', 'events/index.html#event-gallery', 'Original workshop gallery', 'Explore the event photographs'),
        ('https://www.bluzee.xyz/experiencehub', 'testimonials/index.html#participant-voices', 'Original Experience Hub gallery', 'Hear participant feedback')
    ]:
        html = html.replace('href="' + old + '">' + old_label, 'href="' + u(target) + '">' + label)
        html = html.replace('href="' + old + '" target="_blank" rel="noopener">' + old_label, 'href="' + u(target) + '">' + label)
    html = html.replace('</head>', '<link rel="stylesheet" href="' + u('assets/r2-media.css') + '"></head>')
    return html
