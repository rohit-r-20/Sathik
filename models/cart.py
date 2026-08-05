from datetime import datetime
from database.supabase import get_supabase

def format_record(record):
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class CartModel:
    @classmethod
    def get_user_cart(cls, user_id):
        client = get_supabase()
        if client is None:
            return None
        try:
            res = client.table('carts').select('*').eq('user_id', str(user_id)).limit(1).execute()
            if res.data:
                return format_record(res.data[0])
            return None
        except Exception:
            return None

    @classmethod
    def add_item(cls, user_id, product_id, quantity=1, variant_id=None):
        client = get_supabase()
        if client is None:
            return False
        try:
            now = datetime.utcnow().isoformat()
            item = {
                'product_id': str(product_id),
                'quantity': quantity,
                'variant_id': str(variant_id) if variant_id else None,
                'added_at': now
            }
            cart = cls.get_user_cart(user_id)
            if not cart:
                client.table('carts').insert({
                    'user_id': str(user_id),
                    'items': [item],
                    'updated_at': now
                }).execute()
            else:
                items = cart.get('items', [])
                items.append(item)
                client.table('carts').update({
                    'items': items,
                    'updated_at': now
                }).eq('user_id', str(user_id)).execute()
            return True
        except Exception as e:
            print(f"CartModel.add_item error: {e}")
            return False

    @classmethod
    def clear_cart(cls, user_id):
        client = get_supabase()
        if client is None:
            return False
        try:
            client.table('carts').delete().eq('user_id', str(user_id)).execute()
            return True
        except Exception:
            return False
