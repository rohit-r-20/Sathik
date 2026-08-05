from datetime import datetime
from database.supabase import get_supabase

def format_record(record):
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class PaymentModel:
    @classmethod
    def create(cls, data):
        client = get_supabase()
        now = datetime.utcnow().isoformat()
        data['created_at'] = now
        data['status'] = data.get('status', 'initiated')

        if client is None:
            return "mock_payment_id"
        try:
            res = client.table('payments').insert(data).execute()
            if res.data:
                created = format_record(res.data[0])
                return str(created.get('id'))
            return None
        except Exception as e:
            print(f"PaymentModel.create error: {e}")
            return None
