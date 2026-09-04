import os
import json
from datetime import datetime
from database.supabase import get_supabase
from utils.constants import MOCK_PRODUCTS

DATA_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database', 'products_data.json')

_LOCAL_PRODUCTS = None

def format_record(record):
    """Ensure record has both id and _id fields for template backward compatibility."""
    if isinstance(record, dict):
        rec_id = str(record.get('id') or record.get('_id') or '')
        if rec_id:
            record['id'] = rec_id
            record['_id'] = rec_id
        if 'images' in record and isinstance(record['images'], list):
            for img in record['images']:
                if isinstance(img, dict) and not img.get('url'):
                    img['url'] = '/static/images/placeholder.jpg'
        elif not record.get('images'):
            record['images'] = [{'url': '/static/images/placeholder.jpg', 'is_primary': True}]
    return record

def _load_local_products():
    """Load products from persistent JSON file, or initialize with MOCK_PRODUCTS."""
    global _LOCAL_PRODUCTS
    if _LOCAL_PRODUCTS is not None:
        return _LOCAL_PRODUCTS

    if os.path.exists(DATA_FILE_PATH):
        try:
            with open(DATA_FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list) and len(data) > 0:
                    _LOCAL_PRODUCTS = [format_record(p) for p in data]
                    return _LOCAL_PRODUCTS
        except Exception as e:
            print(f"⚠️ Notice reading {DATA_FILE_PATH}: {e}")

    # Initialize from MOCK_PRODUCTS
    _LOCAL_PRODUCTS = [format_record(p.copy()) for p in MOCK_PRODUCTS]
    _save_local_products()
    return _LOCAL_PRODUCTS

def _save_local_products():
    """Atomically save current products to persistent JSON file."""
    global _LOCAL_PRODUCTS
    if _LOCAL_PRODUCTS is None:
        return
    try:
        os.makedirs(os.path.dirname(DATA_FILE_PATH), exist_ok=True)
        with open(DATA_FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(_LOCAL_PRODUCTS, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Notice writing {DATA_FILE_PATH}: {e}")

class ProductService:
    @staticmethod
    def get_all(filter_query=None, sort_field='created_at', sort_order='desc', page=1, limit=12, active_only=True):
        products = _load_local_products()
        client = get_supabase()

        if client is not None:
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
                    if filter_query.get('slug'):
                        if isinstance(filter_query['slug'], dict) and '$ne' in filter_query['slug']:
                            query = query.neq('slug', filter_query['slug']['$ne'])
                        elif isinstance(filter_query['slug'], str):
                            query = query.eq('slug', filter_query['slug'])
                    
                    if filter_query.get('$or'):
                        search_term = None
                        for cond in filter_query['$or']:
                            if 'name' in cond and isinstance(cond['name'], dict):
                                search_term = cond['name'].get('$regex', '')
                        if search_term:
                            query = query.or_(f"name.ilike.%{search_term}%,description.ilike.%{search_term}%,sku.ilike.%{search_term}%,brand_name.ilike.%{search_term}%")

                desc_order = (sort_order in ('desc', -1, 'DESC'))
                query = query.order(sort_field, desc=desc_order)

                start_idx = (page - 1) * limit
                end_idx = start_idx + limit - 1
                query = query.range(start_idx, end_idx)

                res = query.execute()
                remote_products = [format_record(p) for p in (res.data or [])]
                total = res.count if res.count is not None else len(remote_products)
                if remote_products:
                    return remote_products, total
            except Exception as e:
                # Supabase unavailable; seamlessly fall back to local persistent products
                pass

        # Local filtering logic
        results = products.copy()

        if active_only:
            results = [p for p in results if p.get('is_active', True) is True]

        if filter_query:
            if 'business_slug' in filter_query and filter_query['business_slug']:
                results = [p for p in results if p.get('business_slug') == filter_query['business_slug']]

            if 'category_slug' in filter_query and filter_query['category_slug']:
                results = [p for p in results if p.get('category_slug') == filter_query['category_slug']]

            if 'subcategory_slug' in filter_query and filter_query['subcategory_slug']:
                results = [p for p in results if p.get('subcategory_slug') == filter_query['subcategory_slug']]

            if 'brand_slug' in filter_query and filter_query['brand_slug']:
                b_slug = filter_query['brand_slug']
                results = [p for p in results if p.get('brand_slug') == b_slug or b_slug in p.get('available_brand_slugs', [])]

            if 'slug' in filter_query and filter_query['slug']:
                if isinstance(filter_query['slug'], dict) and '$ne' in filter_query['slug']:
                    results = [p for p in results if p.get('slug') != filter_query['slug']['$ne']]
                elif isinstance(filter_query['slug'], str):
                    results = [p for p in results if p.get('slug') == filter_query['slug']]

            if '$or' in filter_query:
                q = ''
                for item in filter_query['$or']:
                    if 'name' in item and isinstance(item['name'], dict):
                        q = item['name'].get('$regex', '')
                    elif 'name' in item and isinstance(item['name'], str):
                        q = item['name']
                if q:
                    q_lower = q.lower()
                    results = [
                        p for p in results 
                        if q_lower in p.get('name', '').lower() 
                        or q_lower in p.get('sku', '').lower()
                        or q_lower in p.get('brand_name', '').lower()
                        or q_lower in p.get('description', '').lower()
                    ]

        total = len(results)

        # Apply sorting
        reverse_sort = (sort_order in ('desc', -1, 'DESC'))
        if sort_field == 'created_at':
            results.sort(key=lambda x: str(x.get('created_at') or '2000-01-01'), reverse=reverse_sort)
        elif sort_field == 'name':
            results.sort(key=lambda x: str(x.get('name', '')).lower(), reverse=reverse_sort)

        # Apply pagination
        start_idx = (page - 1) * limit
        end_idx = start_idx + limit
        paginated = results[start_idx:end_idx]

        return [format_record(r) for r in paginated], total

    @staticmethod
    def get_by_slug(subcategory_slug, product_slug):
        products = _load_local_products()
        client = get_supabase()

        if client is not None:
            try:
                res = client.table('products').select('*')\
                    .eq('slug', product_slug)\
                    .eq('is_active', True)\
                    .limit(1).execute()
                if res.data:
                    return format_record(res.data[0])
            except Exception:
                pass

        for p in products:
            if p.get('slug') == product_slug and p.get('is_active', True):
                return format_record(p)
        return None

    @staticmethod
    def get_by_id(product_id):
        products = _load_local_products()
        client = get_supabase()

        if client is not None:
            try:
                res = client.table('products').select('*').eq('id', product_id).limit(1).execute()
                if res.data:
                    return format_record(res.data[0])
            except Exception:
                pass

        str_id = str(product_id)
        for p in products:
            if str(p.get('id', p.get('_id'))) == str_id:
                return format_record(p)
        return None

    @staticmethod
    def get_featured(limit=8):
        products = _load_local_products()
        client = get_supabase()

        if client is not None:
            try:
                res = client.table('products').select('*')\
                    .eq('is_featured', True)\
                    .eq('is_active', True)\
                    .order('created_at', desc=True)\
                    .limit(limit).execute()
                if res.data:
                    return [format_record(p) for p in res.data]
            except Exception:
                pass

        featured = [p for p in products if p.get('is_active', True) and p.get('is_featured', False)]
        return [format_record(p) for p in featured[:limit]]

    @staticmethod
    def create(data):
        products = _load_local_products()
        now = datetime.utcnow().isoformat()
        
        prod_id = str(data.get('id') or f"p_{data.get('slug', 'prod')}_{int(datetime.utcnow().timestamp())}")
        data['id'] = prod_id
        data['_id'] = prod_id
        data['created_at'] = data.get('created_at') or now
        data['updated_at'] = now
        data['is_active'] = data.get('is_active', True)
        data['is_featured'] = data.get('is_featured', False)
        data['is_new'] = data.get('is_new', True)

        formatted = format_record(data)

        # Attempt remote Supabase insert if online
        client = get_supabase()
        if client is not None:
            try:
                remote_data = formatted.copy()
                client.table('products').insert(remote_data).execute()
            except Exception as e:
                print(f"ProductService remote insert note: {e}")

        # Insert at front of local list so it appears newest first
        products.insert(0, formatted)
        _save_local_products()
        return formatted['id']

    @staticmethod
    def update(product_id, data):
        products = _load_local_products()
        str_id = str(product_id)
        now = datetime.utcnow().isoformat()
        data['updated_at'] = now

        # Attempt remote Supabase update if online
        client = get_supabase()
        if client is not None:
            try:
                client.table('products').update(data).eq('id', product_id).execute()
            except Exception as e:
                print(f"ProductService remote update note: {e}")

        for i, p in enumerate(products):
            if str(p.get('id', p.get('_id'))) == str_id or str(p.get('slug')) == str_id:
                # Merge updates
                products[i].update(data)
                format_record(products[i])
                _save_local_products()
                return True
        return False

    @staticmethod
    def delete(product_id):
        products = _load_local_products()
        str_id = str(product_id)

        # Attempt remote Supabase delete if online
        client = get_supabase()
        if client is not None:
            try:
                client.table('products').delete().eq('id', product_id).execute()
            except Exception as e:
                print(f"ProductService remote delete note: {e}")

        for i, p in enumerate(products):
            if str(p.get('id', p.get('_id'))) == str_id or str(p.get('slug')) == str_id:
                products.pop(i)
                _save_local_products()
                return True
        return False
