from datetime import datetime
from database.supabase import get_supabase
from utils.constants import MOCK_PRODUCTS

def format_record(record):
    """Ensure record has _id field for template backward compatibility."""
    if isinstance(record, dict):
        if 'id' in record and '_id' not in record:
            record['_id'] = str(record['id'])
    return record

class ProductService:
    @staticmethod
    def get_all(filter_query=None, sort_field='created_at', sort_order='desc', page=1, limit=12, active_only=True):
        client = get_supabase()
        if client is None:
            results = MOCK_PRODUCTS.copy()
            if active_only:
                results = [p for p in results if p.get('is_active', True)]
            if filter_query:
                if 'business_slug' in filter_query:
                    results = [p for p in results if p.get('business_slug') == filter_query['business_slug']]
                if 'category_slug' in filter_query:
                    results = [p for p in results if p.get('category_slug') == filter_query['category_slug']]
                if 'brand_slug' in filter_query:
                    results = [p for p in results if p.get('brand_slug') == filter_query['brand_slug'] or filter_query['brand_slug'] in p.get('available_brand_slugs', [])]
                if '$or' in filter_query:
                    q = ''
                    for item in filter_query['$or']:
                        if 'name' in item:
                            q = item['name'].get('$regex', '')
                    if q:
                        results = [p for p in results if q.lower() in p.get('name', '').lower() or q.lower() in p.get('sku', '').lower()]
            return [format_record(r) for r in results], len(results)

        try:
            query = client.table('products').select('*', count='exact')
            if active_only:
                query = query.eq('is_active', True)

            if filter_query:
                if filter_query.get('business_slug'):
                    query = query.eq('business_slug', filter_query['business_slug'])
                if filter_query.get('category_slug'):
                    query = query.eq('category_slug', filter_query['category_slug'])
                if filter_query.get('brand_slug'):
                    query = query.eq('brand_slug', filter_query['brand_slug'])
                if filter_query.get('subcategory_slug'):
                    query = query.eq('subcategory_slug', filter_query['subcategory_slug'])
                
                # Search query handling
                if filter_query.get('$or'):
                    # Extract search term
                    search_term = None
                    for cond in filter_query['$or']:
                        if 'name' in cond and isinstance(cond['name'], dict):
                            search_term = cond['name'].get('$regex', '')
                    if search_term:
                        query = query.or_(f"name.ilike.%{search_term}%,description.ilike.%{search_term}%,sku.ilike.%{search_term}%,brand_name.ilike.%{search_term}%")

            # Sorting
            desc_order = (sort_order == 'desc' or sort_order == -1)
            query = query.order(sort_field, desc=desc_order)

            # Pagination
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit - 1
            query = query.range(start_idx, end_idx)

            res = query.execute()
            products = [format_record(p) for p in (res.data or [])]
            total = res.count if res.count is not None else len(products)
            return products, total
        except Exception as e:
            print(f"ProductService.get_all error: {e}")
            results = MOCK_PRODUCTS.copy()
            if filter_query:
                if 'business_slug' in filter_query:
                    results = [p for p in results if p.get('business_slug') == filter_query['business_slug']]
                if 'category_slug' in filter_query:
                    results = [p for p in results if p.get('category_slug') == filter_query['category_slug']]
                if 'brand_slug' in filter_query:
                    results = [p for p in results if p.get('brand_slug') == filter_query['brand_slug'] or filter_query['brand_slug'] in p.get('available_brand_slugs', [])]
                if 'subcategory_slug' in filter_query:
                    results = [p for p in results if p.get('subcategory_slug') == filter_query['subcategory_slug']]
                if '$or' in filter_query:
                    q = ''
                    for item in filter_query['$or']:
                        if 'name' in item:
                            q = item['name'].get('$regex', '')
                    if q:
                        results = [p for p in results if q.lower() in p.get('name', '').lower() or q.lower() in p.get('sku', '').lower()]
            
            # Pagination
            start_idx = (page - 1) * limit
            end_idx = start_idx + limit
            paginated = results[start_idx:end_idx]
            return [format_record(r) for r in paginated], len(results)

    @staticmethod
    def get_by_slug(subcategory_slug, product_slug):
        client = get_supabase()
        if client is None:
            for p in MOCK_PRODUCTS:
                if p['slug'] == product_slug or p['subcategory_slug'] == subcategory_slug:
                    return format_record(p)
            return format_record(MOCK_PRODUCTS[0]) if MOCK_PRODUCTS else None

        try:
            res = client.table('products').select('*')\
                .eq('subcategory_slug', subcategory_slug)\
                .eq('slug', product_slug)\
                .eq('is_active', True)\
                .limit(1).execute()
            
            if res.data:
                return format_record(res.data[0])
            for p in MOCK_PRODUCTS:
                if p['slug'] == product_slug and p['subcategory_slug'] == subcategory_slug:
                    return format_record(p)
            return None
        except Exception as e:
            print(f"ProductService.get_by_slug error: {e}")
            for p in MOCK_PRODUCTS:
                if p['slug'] == product_slug and p['subcategory_slug'] == subcategory_slug:
                    return format_record(p)
            return None

    @staticmethod
    def get_by_id(product_id):
        client = get_supabase()
        if client is None:
            for p in MOCK_PRODUCTS:
                if str(p.get('id', p.get('_id'))) == str(product_id):
                    return format_record(p)
            return format_record(MOCK_PRODUCTS[0]) if MOCK_PRODUCTS else None

        try:
            res = client.table('products').select('*').eq('id', product_id).limit(1).execute()
            if res.data:
                return format_record(res.data[0])
            return None
        except Exception as e:
            print(f"ProductService.get_by_id error: {e}")
            return None

    @staticmethod
    def get_featured(limit=8):
        client = get_supabase()
        if client is None:
            return [format_record(p) for p in MOCK_PRODUCTS[:limit]]

        try:
            res = client.table('products').select('*')\
                .eq('is_featured', True)\
                .eq('is_active', True)\
                .limit(limit).execute()
            return [format_record(p) for p in (res.data or [])]
        except Exception as e:
            print(f"ProductService.get_featured error: {e}")
            return [format_record(p) for p in MOCK_PRODUCTS[:limit]]

    @staticmethod
    def create(data):
        client = get_supabase()
        if client is not None:
            try:
                now = datetime.utcnow().isoformat()
                data['created_at'] = data.get('created_at', now)
                data['updated_at'] = now
                data['is_active'] = data.get('is_active', True)
                data['is_featured'] = data.get('is_featured', False)
                data['is_new'] = data.get('is_new', False)

                res = client.table('products').insert(data).execute()
                if res.data:
                    created = format_record(res.data[0])
                    return created.get('id')
                return None
            except Exception as e:
                print(f"ProductService.create error: {e}. Falling back to MOCK_PRODUCTS.")

        data['id'] = f"mock_{len(MOCK_PRODUCTS) + 1}"
        data['_id'] = data['id']
        data['is_active'] = data.get('is_active', True)
        data['is_featured'] = data.get('is_featured', False)
        data['is_new'] = data.get('is_new', False)
        MOCK_PRODUCTS.append(data)
        return data['id']

    @staticmethod
    def update(product_id, data):
        client = get_supabase()
        if client is not None:
            try:
                data['updated_at'] = datetime.utcnow().isoformat()
                res = client.table('products').update(data).eq('id', product_id).execute()
                return len(res.data) > 0 if res.data else False
            except Exception as e:
                print(f"ProductService.update error: {e}. Falling back to MOCK_PRODUCTS.")

        for i, p in enumerate(MOCK_PRODUCTS):
            if p.get('id') == product_id or p.get('_id') == product_id:
                MOCK_PRODUCTS[i].update(data)
                return True
        return False

    @staticmethod
    def delete(product_id):
        client = get_supabase()
        if client is not None:
            try:
                res = client.table('products').delete().eq('id', product_id).execute()
                return len(res.data) > 0 if res.data else False
            except Exception as e:
                print(f"ProductService.delete error: {e}. Falling back to MOCK_PRODUCTS.")

        for i, p in enumerate(MOCK_PRODUCTS):
            if p.get('id') == product_id or p.get('_id') == product_id:
                MOCK_PRODUCTS.pop(i)
                return True
        return False
