import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'sathik-groups-secret-key-2024-change-in-production')
    
    # Supabase Configuration
    SUPABASE_URL = os.getenv('SUPABASE_URL', '')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY', '')
    
    # Resend Email Configuration
    RESEND_API_KEY = os.getenv('RESEND_API_KEY', '')
    RESEND_FROM = os.getenv('RESEND_FROM', 'onboarding@resend.dev')
    RESEND_TO = os.getenv('RESEND_TO', 'info@sathikgroups.com')
    
    PORT = int(os.getenv('PORT', 5001))
    
    # Upload Settings
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max upload size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'svg', 'pdf'}
    
    # Cloudinary Config (Optional)
    CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME', '')
    CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY', '')
    CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET', '')
    
    # Pagination Defaults
    PRODUCTS_PER_PAGE = 12
    ADMIN_ITEMS_PER_PAGE = 20
