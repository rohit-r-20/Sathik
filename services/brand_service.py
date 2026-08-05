from datetime import datetime
from database.supabase import get_supabase
from utils.constants import BRANDS_LIST

def format_record(record):
    """Ensure record has _id field for template backward compatibility."""
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class BrandService:
    @staticmethod
    def get_all(featured_only=False, business_slug=None):
        client = get_supabase()
        if client is None:
            results = BRANDS_LIST.copy()
            if featured_only:
                results = [b for b in results if b.get('featured')]
            if business_slug:
                results = [b for b in results if business_slug in b.get('businesses', [])]
            return [format_record(b) for b in results]

        try:
            query = client.table('brands').select('*').eq('is_active', True)
            if featured_only:
                query = query.eq('featured', True)
            if business_slug:
                query = query.contains('businesses', [business_slug])

            res = query.order('name', desc=False).execute()
            return [format_record(b) for b in (res.data or [])]
        except Exception as e:
            print(f"BrandService.get_all error: {e}")
            results = BRANDS_LIST.copy()
            if featured_only:
                results = [b for b in results if b.get('featured')]
            return [format_record(b) for b in results]

    @staticmethod
    def get_by_slug(slug):
        client = get_supabase()
        if client is None:
            for b in BRANDS_LIST:
                if b['slug'] == slug:
                    return format_record(b)
            return format_record(BRANDS_LIST[0]) if BRANDS_LIST else None

        try:
            res = client.table('brands').select('*').eq('slug', slug).eq('is_active', True).limit(1).execute()
            if res.data:
                return format_record(res.data[0])
            return None
        except Exception as e:
            print(f"BrandService.get_by_slug error: {e}")
            return None

    @staticmethod
    def create(data):
        client = get_supabase()
        if client is None:
            BRANDS_LIST.append(data)
            return data.get('slug')

        try:
            data['created_at'] = datetime.utcnow().isoformat()
            data['is_active'] = data.get('is_active', True)
            res = client.table('brands').insert(data).execute()
            if res.data:
                created = format_record(res.data[0])
                return created.get('id', created.get('slug'))
            return None
        except Exception as e:
            print(f"BrandService.create error: {e}")
            return None
