from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from database.supabase import get_supabase

def format_record(record):
    """Ensure record has _id field for template backward compatibility."""
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class UserService:
    @staticmethod
    def find_by_email(email):
        client = get_supabase()
        clean_email = email.lower().strip()

        if client is None:
            if clean_email == 'admin@sathikgroups.com':
                return {
                    'id': 'demo_super_admin_id',
                    '_id': 'demo_super_admin_id',
                    'name': 'Super Admin (Demo)',
                    'email': 'admin@sathikgroups.com',
                    'password_hash': generate_password_hash('ChangeMe@2024!'),
                    'role': 'super_admin'
                }
            return None

        try:
            res = client.table('users').select('*').eq('email', clean_email).limit(1).execute()
            if res.data and len(res.data) > 0:
                return format_record(res.data[0])
            
            # Fallback if users table is empty or missing admin
            if clean_email == 'admin@sathikgroups.com':
                return {
                    'id': 'demo_super_admin_id',
                    '_id': 'demo_super_admin_id',
                    'name': 'Super Admin (Demo)',
                    'email': 'admin@sathikgroups.com',
                    'password_hash': generate_password_hash('ChangeMe@2024!'),
                    'role': 'super_admin'
                }
            return None
        except Exception as e:
            print(f"UserService.find_by_email error: {e}")
            if clean_email == 'admin@sathikgroups.com':
                return {
                    'id': 'demo_super_admin_id',
                    '_id': 'demo_super_admin_id',
                    'name': 'Super Admin (Demo)',
                    'email': 'admin@sathikgroups.com',
                    'password_hash': generate_password_hash('ChangeMe@2024!'),
                    'role': 'super_admin'
                }
            return None

    @staticmethod
    def find_by_id(user_id):
        client = get_supabase()
        if client is None:
            return None

        try:
            res = client.table('users').select('*').eq('id', user_id).limit(1).execute()
            if res.data and len(res.data) > 0:
                return format_record(res.data[0])
            return None
        except Exception as e:
            print(f"UserService.find_by_id error: {e}")
            return None

    @staticmethod
    def create(name, email, password, role='customer', permissions=None):
        client = get_supabase()
        clean_email = email.lower().strip()

        existing = UserService.find_by_email(clean_email)
        if existing and existing.get('id') != 'demo_super_admin_id':
            return None

        now = datetime.utcnow().isoformat()
        user_data = {
            'name': name.strip(),
            'email': clean_email,
            'password_hash': generate_password_hash(password),
            'role': role,
            'permissions': permissions or [],
            'is_active': True,
            'created_at': now,
            'updated_at': now
        }

        if client is None:
            user_data['id'] = f"user_{clean_email}"
            return user_data['id']

        try:
            res = client.table('users').insert(user_data).execute()
            if res.data:
                created = format_record(res.data[0])
                return str(created.get('id'))
            return None
        except Exception as e:
            print(f"UserService.create error: {e}")
            return None

    @staticmethod
    def verify_password(user, password):
        if not user:
            return False
        pwd_hash = user.get('password_hash', '')
        if not pwd_hash:
            return False
        return check_password_hash(pwd_hash, password)
