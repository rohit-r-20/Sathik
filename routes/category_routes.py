from flask import Blueprint, jsonify, render_template, abort
from models.category import CategoryModel, SubcategoryModel
from models.product import ProductModel
from models.brand import BrandModel
from utils.constants import BUSINESSES, COMPANY_INFO
from services.category_service import SubcategoryService

category_bp = Blueprint('category', __name__)

@category_bp.route('/stores')
def store_list():
    categories = CategoryModel.find_all()
    subcategories = SubcategoryService.get_all()
    
    # Group categories by store/business vertical
    stores_data = []
    for biz in BUSINESSES:
        biz_cats = [c for c in categories if c.get('business_slug') == biz['slug']]
        for c in biz_cats:
            c['subcategories'] = [s for s in subcategories if s.get('category_slug') == c['slug']]
        stores_data.append({
            'business': biz,
            'categories': biz_cats
        })

    return render_template(
        'stores.html',
        stores_data=stores_data,
        businesses=BUSINESSES,
        company=COMPANY_INFO
    )

@category_bp.route('/stores/<business_slug>')
def store_detail(business_slug):
    biz = next((b for b in BUSINESSES if b['slug'] == business_slug), None)
    if not biz:
        abort(404)

    categories = CategoryModel.find_all(business_slug=business_slug)
    subcategories = SubcategoryService.get_by_business(business_slug)

    # Attach subcategories to each category
    for c in categories:
        c['subcategories'] = [s for s in subcategories if s.get('category_slug') == c['slug']]

    # Fetch store products
    products, total = ProductModel.find_all(
        filter_query={'business_slug': business_slug},
        limit=12
    )

    brands = BrandModel.find_all(business_slug=business_slug)

    return render_template(
        'store_detail.html',
        business=biz,
        categories=categories,
        products=products,
        total_products=total,
        brands=brands,
        company=COMPANY_INFO
    )

@category_bp.route('/stores/<business_slug>/<category_slug>')
def store_category_detail(business_slug, category_slug):
    biz = next((b for b in BUSINESSES if b['slug'] == business_slug), None)
    if not biz:
        abort(404)

    category = CategoryModel.find_by_slug(category_slug)
    if not category:
        abort(404)

    subcategories = SubcategoryService.get_by_category(category_slug)
    products, total = ProductModel.find_all(
        filter_query={'business_slug': business_slug, 'category_slug': category_slug},
        limit=12
    )

    categories = CategoryModel.find_all(business_slug=business_slug)

    return render_template(
        'store_detail.html',
        business=biz,
        current_category=category,
        categories=categories,
        subcategories=subcategories,
        products=products,
        total_products=total,
        company=COMPANY_INFO
    )

# API JSON endpoints for backward compatibility
@category_bp.route('/categories')
def category_list():
    categories = CategoryModel.find_all()
    return jsonify({'success': True, 'data': categories})

@category_bp.route('/categories/<slug>')
def category_detail(slug):
    category = CategoryModel.find_by_slug(slug)
    if not category:
        return jsonify({'success': False, 'message': 'Category not found'}), 404
    subcategories = SubcategoryModel.find_by_category(category['_id'])
    return jsonify({'success': True, 'data': {'category': category, 'subcategories': subcategories}})

