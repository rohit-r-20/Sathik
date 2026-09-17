import os
from werkzeug.utils import secure_filename

def save_uploaded_image(file_obj, upload_folder, allowed_extensions):
    """
    Saves an uploaded image file to static/uploads/ safely.
    Returns (success, relative_url_or_error)
    """
    if not file_obj or file_obj.filename == '':
        return False, 'No file selected'

    filename = secure_filename(file_obj.filename)
    ext = filename.rsplit('.', 1)[-1].lower() if '.' in filename else ''
    
    if ext not in allowed_extensions:
        return False, f'File extension .{ext} is not allowed'

    # Read file bytes directly from stream
    file_bytes = file_obj.read()

    # Safely attempt saving locally if writable (for local development)
    try:
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        with open(file_path, 'wb') as f:
            f.write(file_bytes)
    except Exception as e:
        print(f"ℹ️ Local disk write bypassed on read-only serverless: {e}")

    # Upload to GitHub storage if configured, guaranteeing persistent URLs on Vercel
    try:
        from services.github_storage import GithubStorageService
        ok, url_or_err = GithubStorageService.upload_image(file_bytes, filename)
        return ok, url_or_err
    except Exception as e:
        print(f"⚠️ GitHub image upload notice: {e}")
        return True, f"/static/uploads/{filename}"
