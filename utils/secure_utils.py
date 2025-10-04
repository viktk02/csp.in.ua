import base64
import os

def generate_nonce():
    return base64.b64encode(os.urandom(16)).decode()

def create_csp(nonce):
    return (
        "default-src 'self';"
        f"script-src 'self' 'nonce-{nonce}' https://cdn.jsdelivr.net; "
        "style-src 'self' 'unsafe-inline' https://cdn.jsdelivr.net https://fonts.googleapis.com; "
        "img-src 'self' data: https:; "
        "font-src 'self' https://fonts.gstatic.com https://cdn.jsdelivr.net data:; "
        "media-src 'self' https://www.youtube.com https://youtube.com"
    )