from datetime import datetime
from database.supabase import get_supabase

def format_record(record):
    """Ensure record has _id field for template backward compatibility."""
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class SettingService:
    @staticmethod
    def get_all_public():
        client = get_supabase()
        if client is None:
            return {}

        try:
            res = client.table('settings').select('*').eq('is_public', True).execute()
            items = res.data or []
            return {s['key']: s['value'] for s in items if 'key' in s and 'value' in s}
        except Exception as e:
            print(f"SettingService.get_all_public error: {e}")
            return {}

    @staticmethod
    def get_all():
        client = get_supabase()
        if client is None:
            return []

        try:
            res = client.table('settings').select('*').execute()
            return [format_record(s) for s in (res.data or [])]
        except Exception as e:
            print(f"SettingService.get_all error: {e}")
            return []

    @staticmethod
    def get_value(key, default=None):
        client = get_supabase()
        if client is None:
            return default

        try:
            res = client.table('settings').select('value').eq('key', key).limit(1).execute()
            if res.data and len(res.data) > 0:
                return res.data[0].get('value', default)
            return default
        except Exception as e:
            print(f"SettingService.get_value error: {e}")
            return default

    @staticmethod
    def set_value(key, value, group='general', label='', is_public=True):
        client = get_supabase()
        if client is None:
            return False

        try:
            data = {
                'key': key,
                'value': value,
                'group': group,
                'label': label or key.title(),
                'is_public': is_public,
                'updated_at': datetime.utcnow().isoformat()
            }
            res = client.table('settings').upsert(data, on_conflict='key').execute()
            return True
        except Exception as e:
            print(f"SettingService.set_value error: {e}")
            return False
