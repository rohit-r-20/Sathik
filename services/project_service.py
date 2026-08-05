from datetime import datetime
from database.supabase import get_supabase

def format_record(record):
    """Ensure record has _id field for template backward compatibility."""
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class ProjectService:
    @staticmethod
    def get_all(featured_only=False):
        client = get_supabase()
        if client is None:
            return []

        try:
            query = client.table('projects').select('*').eq('is_active', True)
            if featured_only:
                query = query.eq('is_featured', True)

            res = query.order('order', desc=False).execute()
            return [format_record(p) for p in (res.data or [])]
        except Exception as e:
            print(f"ProjectService.get_all error: {e}")
            return []

    @staticmethod
    def get_by_slug(slug):
        client = get_supabase()
        if client is None:
            return None

        try:
            res = client.table('projects').select('*').eq('slug', slug).eq('is_active', True).limit(1).execute()
            if res.data:
                return format_record(res.data[0])
            return None
        except Exception as e:
            print(f"ProjectService.get_by_slug error: {e}")
            return None

    @staticmethod
    def create(data):
        client = get_supabase()
        if client is None:
            return None

        try:
            data['created_at'] = datetime.utcnow().isoformat()
            data['is_active'] = data.get('is_active', True)
            res = client.table('projects').insert(data).execute()
            if res.data:
                created = format_record(res.data[0])
                return created.get('id', created.get('slug'))
            return None
        except Exception as e:
            print(f"ProjectService.create error: {e}")
            return None
