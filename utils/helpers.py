import re
import urllib.parse
from datetime import datetime

def generate_slug(text):
    """
    Converts a title or name into a URL-friendly slug.
    Example: "CPVC Pipes 1/2 inch" -> "cpvc-pipes-1-2-inch"
    """
    if not text:
        return ''
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    text = re.sub(r'^-+|-+$', '', text)
    return text

def build_whatsapp_url(phone, message):
    """
    Generates a WhatsApp click-to-chat link.
    """
    sanitized_phone = re.sub(r'\D', '', phone)
    encoded_message = urllib.parse.quote(message)
    return f"https://wa.me/{sanitized_phone}?text={encoded_message}"

def build_product_whatsapp_message(product_name, sku):
    """
    Formats WhatsApp product quote request text.
    """
    return f"Hi, I'm interested in the following product from Sathik Groups:\n\n*Product:* {product_name}\n*SKU:* {sku}\n\nPlease share availability and quote."

def format_date(dt):
    """
    Formats a datetime object to a readable string.
    """
    if isinstance(dt, datetime):
        return dt.strftime('%b %d, %Y %I:%M %p')
    return str(dt) if dt else ''

def parse_id(id_str):
    """
    Safely stringifies an ID.
    """
    return str(id_str) if id_str else None
