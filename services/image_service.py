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

    os.makedirs(upload_folder, exist_ok=True)
    file_path = os.path.join(upload_folder, filename)
    file_obj.save(file_path)

    relative_url = f"/static/uploads/{filename}"
    return True, relative_url
