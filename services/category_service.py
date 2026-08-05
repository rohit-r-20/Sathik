from datetime import datetime
from database.supabase import get_supabase
from utils.constants import MOCK_CATEGORIES

def format_record(record):
    """Ensure record has _id field for template backward compatibility."""
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class CategoryService:
    @staticmethod
    def get_all(business_slug=None):
        client = get_supabase()
        if client is None:
            results = MOCK_CATEGORIES.copy()
            if business_slug:
                results = [c for c in results if c.get('business_slug') == business_slug]
            return [format_record(c) for c in results]

        try:
            query = client.table('categories').select('*').eq('is_active', True)
            if business_slug:
                query = query.eq('business_slug', business_slug)
            res = query.order('order', desc=False).execute()
            return [format_record(c) for c in (res.data or [])]
        except Exception as e:
            print(f"CategoryService.get_all error: {e}")
            results = MOCK_CATEGORIES.copy()
            if business_slug:
                results = [c for c in results if c.get('business_slug') == business_slug]
            return [format_record(c) for c in results]

    @staticmethod
    def get_by_slug(slug):
        client = get_supabase()
        if client is None:
            for c in MOCK_CATEGORIES:
                if c['slug'] == slug:
                    return format_record(c)
            return format_record(MOCK_CATEGORIES[0]) if MOCK_CATEGORIES else None

        try:
            res = client.table('categories').select('*').eq('slug', slug).eq('is_active', True).limit(1).execute()
            if res.data:
                return format_record(res.data[0])
            return None
        except Exception as e:
            print(f"CategoryService.get_by_slug error: {e}")
            return None

    @staticmethod
    def create(data):
        client = get_supabase()
        if client is None:
            return data.get('slug')

        try:
            data['created_at'] = datetime.utcnow().isoformat()
            data['is_active'] = data.get('is_active', True)
            res = client.table('categories').insert(data).execute()
            if res.data:
                created = format_record(res.data[0])
                return created.get('id', created.get('slug'))
            return None
        except Exception as e:
            print(f"CategoryService.create error: {e}")
            return None

class SubcategoryService:
    @staticmethod
    def get_by_category(category_id_or_slug):
        client = get_supabase()
        if client is None:
            return []

        try:
            res = client.table('subcategories').select('*')\
                .or_(f"category_id.eq.{category_id_or_slug},category_slug.eq.{category_id_or_slug}")\
                .eq('is_active', True)\
                .order('order', desc=False).execute()
            return [format_record(s) for s in (res.data or [])]
        except Exception as e:
            print(f"SubcategoryService.get_by_category error: {e}")
            return []

    @staticmethod
    def get_all():
        client = get_supabase()
        if client is None:
            return []

        try:
            res = client.table('subcategories').select('*').eq('is_active', True).order('order', desc=False).execute()
            return [format_record(s) for s in (res.data or [])]
        except Exception as e:
            print(f"SubcategoryService.get_all error: {e}")
            return []

    @staticmethod
    def create(data):
        client = get_supabase()
        if client is None:
            return data.get('slug')

        try:
            data['created_at'] = datetime.utcnow().isoformat()
            data['is_active'] = data.get('is_active', True)
            res = client.table('subcategories').insert(data).execute()
            if res.data:
                created = format_record(res.data[0])
                return created.get('id', created.get('slug'))
            return None
        except Exception as e:
            print(f"SubcategoryService.create error: {e}")
            return None
