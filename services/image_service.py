import os
import io
import base64
from werkzeug.utils import secure_filename
from PIL import Image

def optimize_image_to_data_url(file_bytes, max_dim=800, quality=82):
    """
    Optimizes and compresses an image into a compact Base64 WebP/JPEG data URL.
    Embeds directly into product data so images load instantly anywhere without 404s.
    """
    try:
        img = Image.open(io.BytesIO(file_bytes))
        if img.mode in ('RGBA', 'LA', 'P'):
            img = img.convert('RGBA')
            fmt = 'WEBP'
            mime = 'image/webp'
        else:
            img = img.convert('RGB')
            fmt = 'WEBP'
            mime = 'image/webp'

        img.thumbnail((max_dim, max_dim), Image.Resampling.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, format=fmt, quality=quality, optimize=True)
        b64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        return f"data:{mime};base64,{b64}"
    except Exception as e:
        print(f"⚠️ Image base64 optimization error: {e}")
        b64 = base64.b64encode(file_bytes).decode('utf-8')
        return f"data:image/jpeg;base64,{b64}"

def save_uploaded_image(file_obj, upload_folder, allowed_extensions):
    """
    Saves or optimizes an uploaded image file safely.
    Returns (success, url_or_error)
    """
    if not file_obj or file_obj.filename == '':
        return False, 'No file selected'

    filename = secure_filename(file_obj.filename)
    ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
    
    if ext not in allowed_extensions:
        return False, f'File extension .{ext} is not allowed'

    # Read raw bytes directly from upload stream
    file_bytes = file_obj.read()

    # Safely attempt saving locally if writable (for local dev and git commits)
    try:
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(file_bytes)
    except Exception as e:
        print(f"ℹ️ Local disk write bypassed on read-only serverless: {e}")

    # 1. Upload to GitHub repository if GITHUB_TOKEN is configured
    try:
        from services.github_storage import GithubStorageService
        if GithubStorageService.is_configured():
            ok, url_or_err = GithubStorageService.upload_image(file_bytes, filename)
            if ok and (url_or_err.startswith('http://') or url_or_err.startswith('https://')):
                return True, url_or_err
    except Exception as e:
        print(f"⚠️ GitHub image upload notice: {e}")

    # 2. Resilient Cloud Fallback: Convert to self-contained optimized WebP Data URI
    # This guarantees the image loads immediately without requiring serverless disk storage
    data_url = optimize_image_to_data_url(file_bytes)
    return True, data_url
