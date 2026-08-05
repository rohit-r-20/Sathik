import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

supabase: Client = None

def init_supabase(app=None):
    """
    Initialize and export reusable Supabase client using environment variables.
    """
    global supabase
    
    url = os.getenv('SUPABASE_URL')
    key = os.getenv('SUPABASE_KEY')

    if app:
        url = app.config.get('SUPABASE_URL', url)
        key = app.config.get('SUPABASE_KEY', key)

    if not url or not key or 'your-supabase-project' in url:
        print("⚠️ Supabase Notice: SUPABASE_URL or SUPABASE_KEY not fully configured in .env.")
        print("💡 Application running with mock fallbacks for client preview.")
        supabase = None
        return None

    try:
        supabase = create_client(url, key)
        print("✅ Supabase client initialized successfully.")
        return supabase
    except Exception as e:
        print(f"⚠️ Supabase Connection Warning: {e}")
        supabase = None
        return None

def get_supabase() -> Client:
    """
    Returns the initialized Supabase client instance.
    """
    global supabase
    if supabase is None:
        init_supabase()
    return supabase
