from flask import Blueprint, render_template, request, abort
from models.product import ProductModel
from models.category import CategoryModel
from models.brand import BrandModel
from utils.constants import BUSINESSES, COMPANY_INFO
from utils.helpers import build_whatsapp_url, build_product_whatsapp_message

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def product_list():
    business_filter = request.args.get('business', '').strip()
    category_filter = request.args.get('category', '').strip()
    subcategory_filter = request.args.get('subcategory', '').strip()
    brand_filter = request.args.get('brand', '').strip()
    search_query = request.args.get('q', '').strip()
    page = int(request.args.get('page', 1))
    limit = 12

    filter_query = {}
    if business_filter:
        filter_query['business_slug'] = business_filter
    if category_filter:
        filter_query['category_slug'] = category_filter
    if subcategory_filter:
        filter_query['subcategory_slug'] = subcategory_filter
    if brand_filter:
        filter_query['brand_slug'] = brand_filter
    if search_query:
        filter_query['$or'] = [
            {'name': {'$regex': search_query, '$options': 'i'}},
            {'description': {'$regex': search_query, '$options': 'i'}},
            {'brand_name': {'$regex': search_query, '$options': 'i'}},
            {'sku': {'$regex': search_query, '$options': 'i'}}
        ]

    products, total = ProductModel.find_all(
        filter_query=filter_query,
        page=page,
        limit=limit
    )

    categories = CategoryModel.find_all(business_slug=business_filter or None)
    
    # Fetch subcategories for active category/business
    from services.category_service import SubcategoryService
    if category_filter:
        subcategories = SubcategoryService.get_by_category(category_filter)
    elif business_filter:
        subcategories = SubcategoryService.get_by_business(business_filter)
    else:
        subcategories = SubcategoryService.get_all()

    brands = BrandModel.find_all(business_slug=business_filter or None)

    total_pages = (total + limit - 1) // limit if total > 0 else 1

    return render_template(
        'products.html',
        products=products,
        businesses=BUSINESSES,
        categories=categories,
        subcategories=subcategories,
        brands=brands,
        current_business=business_filter,
        current_category=category_filter,
        current_subcategory=subcategory_filter,
        current_brand=brand_filter,
        search_query=search_query,
        page=page,
        total_pages=total_pages,
        total_products=total,
        company=COMPANY_INFO
    )


@product_bp.route('/products/<subcategory_slug>/<product_slug>')
def product_detail(subcategory_slug, product_slug):
    product = ProductModel.find_by_slug(subcategory_slug, product_slug)
    if not product:
        abort(404)

    # Related products from same subcategory
    related_products, _ = ProductModel.find_all(
        filter_query={'subcategory_slug': subcategory_slug, 'slug': {'$ne': product_slug}},
        limit=4
    )

    # WhatsApp pre-filled enquiry text
    wa_message = build_product_whatsapp_message(product.get('name', ''), product.get('sku', ''))
    wa_url = build_whatsapp_url(COMPANY_INFO['whatsapp'], wa_message)

    return render_template(
        'product.html',
        product=product,
        related_products=related_products,
        whatsapp_url=wa_url,
        company=COMPANY_INFO
    )
