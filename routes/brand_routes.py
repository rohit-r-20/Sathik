from flask import Blueprint, render_template, abort
from models.brand import BrandModel
from models.product import ProductModel
from utils.constants import COMPANY_INFO

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
    products, total = ProductModel.find_all(filter_query={'brand_slug': slug}, limit=24)
    return render_template(
        'products.html',
        products=products,
        current_brand=slug,
        selected_brand=brand,
        total_products=total,
        company=COMPANY_INFO
    )
