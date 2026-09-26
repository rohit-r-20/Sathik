from flask import Blueprint, render_template, abort, request
from models.brand import BrandModel
from models.product import ProductModel
from utils.constants import COMPANY_INFO
from utils.brand_seo import get_brand_seo

brand_bp = Blueprint('brand', __name__)

@brand_bp.route('/brands')
def brand_list():
    brands = BrandModel.find_all()
    featured_brands = [b for b in brands if b.get('featured')]
    other_brands = [b for b in brands if not b.get('featured')]
    return render_template(
        'brands.html',
        featured_brands=featured_brands,
        other_brands=other_brands,
        brands=brands,
        company=COMPANY_INFO
    )

@brand_bp.route('/brands/<slug>')
def brand_detail(slug):
    brand = BrandModel.find_by_slug(slug)
    if not brand:
        abort(404)
    page = int(request.args.get('page', 1))
    limit = 24
    products, total = ProductModel.find_all(filter_query={'brand_slug': slug}, page=page, limit=limit)
    total_pages = (total + limit - 1) // limit if total > 0 else 1
    brand_seo = get_brand_seo(brand)
    return render_template(
        'brand_detail.html',
        brand=brand,
        brand_seo=brand_seo,
        products=products,
        current_brand=slug,
        selected_brand=brand,
        total_products=total,
        total_pages=total_pages,
        page=page,
        company=COMPANY_INFO
    )

