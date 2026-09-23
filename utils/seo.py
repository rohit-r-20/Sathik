"""
SEO Utilities for SathikGroups Platform.
Generates canonical URLs and manages SEO metadata.
"""
from flask import request, url_for

CANONICAL_DOMAIN = 'https://sathikgroups.com'

# Explicit set of public indexable routes that have canonical URLs
PUBLIC_ENDPOINTS = {
    'home.index',
    'product.product_list',
    'category.store_list',
    'category.store_detail',
    'category.store_category_detail',
    'brand.brand_list',
    'brand.brand_detail',
    'product.product_detail',
    'home.projects'
}

# Endpoints that support meaningful product pagination
PAGINATED_ENDPOINTS = {
    'product.product_list',
    'brand.brand_detail'
}

def get_canonical_url():
    """
    Computes the canonical HTTPS URL for the current active request.

    Specifications:
    - Always uses HTTPS and domain https://sathikgroups.com.
    - Strips tracking parameters (utm_*, gclid, fbclid, etc.).
    - Preserves meaningful pagination (?page=N where N > 1) on product/brand listing pages,
      ensuring Googlebot indexes paginated product listings rather than ignoring them as duplicates.
    - Consolidates page 1 (?page=1) to the clean base URL without query parameters.
    - Homepage canonical is strictly 'https://sathikgroups.com/'.
    - All other canonical URLs omit trailing slashes.
    - Returns None for non-canonical, admin, auth, or error pages.
    """
    try:
        if not request or not request.endpoint:
            return None

        endpoint = request.endpoint

        if endpoint not in PUBLIC_ENDPOINTS:
            return None

        view_args = request.view_args.copy() if request.view_args else {}
        canonical_path = url_for(endpoint, **view_args)

        if canonical_path == '/':
            return f"{CANONICAL_DOMAIN}/"

        canonical_path = canonical_path.rstrip('/')
        base_canonical = f"{CANONICAL_DOMAIN}{canonical_path}"

        # Handle pagination on listing pages
        if endpoint in PAGINATED_ENDPOINTS:
            raw_page = request.args.get('page')
            if raw_page:
                try:
                    page_val = int(raw_page)
                    if page_val > 1:
                        return f"{base_canonical}?page={page_val}"
                except (ValueError, TypeError):
                    pass

        return base_canonical
    except Exception:
        return None
