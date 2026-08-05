from datetime import datetime, timezone
from database.supabase import get_supabase

def format_record(record):
    """Ensure record has _id field for template backward compatibility."""
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class EnquiryService:
    @staticmethod
    def create_enquiry(data):
        """
        Inserts one enquiry row into the Supabase 'enquiries' table.
        Returns True on success, False on error.
        """
        client = get_supabase()
        if client is None:
            print("EnquiryService.create_enquiry: Supabase client is offline (preview mode).")
            return True

        try:
            now = datetime.now(timezone.utc).isoformat()
            # Map clean fields for Supabase table schema (column: 'mobile')
            record = {
                'customer_name': data.get('customer_name') or data.get('name') or '',
                'mobile': data.get('mobile_number') or data.get('mobile') or data.get('phone') or '',
                'email': data.get('email', '').strip() if data.get('email') else None,
                'address': data.get('address', '').strip() if data.get('address') else None,
                'interested_in': data.get('interested_in', '').strip() if data.get('interested_in') else None,
                'product_name': data.get('product_name', '').strip() if data.get('product_name') else None,
                'preferred_contact': data.get('preferred_contact', 'WhatsApp Message').strip(),
                'message': data.get('message', '').strip() if data.get('message') else None,
                'page_url': data.get('page_url', '').strip() if data.get('page_url') else None,
                'status': 'New',
                'created_at': data.get('created_at') or now
            }

            res = client.table('enquiries').insert(record).execute()
            if res.data:
                return True
            return True
        except Exception as e:
            print(f"EnquiryService.create_enquiry error inserting into Supabase: {e}")
            return False

    @staticmethod
    def create(data):
        """Legacy compatibility wrapper for existing model calls."""
        return EnquiryService.create_enquiry(data)

    @staticmethod
    def get_all(status=None, page=1, limit=20):
        client = get_supabase()
        if client is None:
            return [], 0

        try:
            query = client.table('enquiries').select('*', count='exact')
            if status:
                query = query.eq('status', status)

            query = query.order('created_at', desc=True)
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit - 1
            query = query.range(start_idx, end_idx)

            res = query.execute()
            enquiries = [format_record(e) for e in (res.data or [])]
            total = res.count if res.count is not None else len(enquiries)
            return enquiries, total
        except Exception as e:
            print(f"EnquiryService.get_all error: {e}")
            return [], 0

    @staticmethod
    def update_status(enquiry_id, status, notes=None):
        client = get_supabase()
        if client is None:
            return True

        try:
            update_data = {
                'status': status
            }
            if notes:
                update_data['admin_notes'] = notes

            res = client.table('enquiries').update(update_data).eq('id', enquiry_id).execute()
            return len(res.data) > 0 if res.data else False
        except Exception as e:
            print(f"EnquiryService.update_status error: {e}")
            return False

    @staticmethod
    def get_stats():
        client = get_supabase()
        if client is None:
            return {'total': 0, 'new': 0, 'read': 0, 'responded': 0, 'closed': 0}

        try:
            res_all = client.table('enquiries').select('id, status').execute()
            items = res_all.data or []
            total = len(items)
            new_count = sum(1 for i in items if str(i.get('status')).lower() in ('new', 'new'))
            read_count = sum(1 for i in items if str(i.get('status')).lower() == 'read')
            responded_count = sum(1 for i in items if str(i.get('status')).lower() == 'responded')
            closed_count = sum(1 for i in items if str(i.get('status')).lower() == 'closed')

            return {
                'total': total,
                'new': new_count,
                'read': read_count,
                'responded': responded_count,
                'closed': closed_count
            }
        except Exception as e:
            print(f"EnquiryService.get_stats error: {e}")
            return {'total': 0, 'new': 0, 'read': 0, 'responded': 0, 'closed': 0}
