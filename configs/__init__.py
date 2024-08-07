import os
from dotenv import load_dotenv
load_dotenv()
import json

def debugmode() -> bool:

    debug = os.getenv('DEBUG', 'False').lower() in (
        'true', '1', 't', 'y', 'yes')
    return debug


def csp() -> dict[str]:

    csp_vars = {
    'default-src': [
        '\'self\''
    ],
    'script-src': [
        '\'self\'',
        'https://cdn.jsdelivr.net',
        'https://cdnjs.cloudflare.com',
        'https://cdn.datatables.net',
        'https://unpkg.com',
        'https://code.jquery.com',
        'https://use.fontawesome.com',
        '',
        '\'unsafe-inline\'',
    ],
    'style-src': [
        '\'self\'',
        'https://cdn.jsdelivr.net',
        'https://cdnjs.cloudflare.com',
        'https://cdn.datatables.net',
        'https://unpkg.com',
        '\'unsafe-inline\'',
    ],
    'img-src': [
        '\'self\'',
        'data:',
        'https://cdn.jsdelivr.net',
        'https://cdnjs.cloudflare.com',
        'https://cdn.datatables.net',
        'https://unpkg.com',
        'https://cdn-icons-png.flaticon.com',
        'http: //guardepi.robotz.dev',
    ],
    'connect-src': [
        '\'self\'',
        'https://cdn.jsdelivr.net',
        'https://cdnjs.cloudflare.com',
        'https://cdn.datatables.net',
        'https://unpkg.com',
    ],
    'frame-src': [
        '\'self\'',
        'https://guardepi.robotz.dev',
    ]
}
    return csp_vars
