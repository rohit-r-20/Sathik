from datetime import datetime
from database.supabase import get_supabase

def format_record(record):
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class ReviewModel:
    @classmethod
    def find_by_product(cls, product_id):
        client = get_supabase()
        if client is None:
            return []
        try:
            res = client.table('reviews').select('*').eq('product_id', str(product_id)).eq('is_approved', True).order('created_at', desc=True).execute()
            return [format_record(r) for r in (res.data or [])]
        except Exception:
            return []

    @classmethod
    def create(cls, data):
        client = get_supabase()
        now = datetime.utcnow().isoformat()
        data['created_at'] = now
        data['is_approved'] = data.get('is_approved', False)

        if client is None:
            return "mock_review_id"
        try:
            res = client.table('reviews').insert(data).execute()
            if res.data:
                created = format_record(res.data[0])
                return str(created.get('id'))
            return None
        except Exception as e:
            print(f"ReviewModel.create error: {e}")
            return None
