from datetime import datetime
from database.supabase import get_supabase

def format_record(record):
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class OrderModel:
    @classmethod
    def create(cls, data):
        client = get_supabase()
        now = datetime.utcnow().isoformat()
        data['created_at'] = now
        data['updated_at'] = now
        data['status'] = data.get('status', 'pending')
        data['payment_status'] = data.get('payment_status', 'unpaid')
        
        if client is None:
            return "mock_order_id"
        try:
            res = client.table('orders').insert(data).execute()
            if res.data:
                created = format_record(res.data[0])
                return str(created.get('id'))
            return None
        except Exception as e:
            print(f"OrderModel.create error: {e}")
            return None

    @classmethod
    def find_by_user(cls, user_id):
        client = get_supabase()
        if client is None:
            return []
        try:
            res = client.table('orders').select('*').eq('user_id', str(user_id)).order('created_at', desc=True).execute()
            return [format_record(o) for o in (res.data or [])]
        except Exception:
            return []
