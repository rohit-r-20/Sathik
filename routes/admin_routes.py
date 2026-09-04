from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify, current_app, abort
from models.product import ProductModel
from models.brand import BrandModel
from models.category import CategoryModel
from models.enquiry import EnquiryModel
from models.project import ProjectModel
from models.settings import SettingModel
from utils.constants import BUSINESSES
from utils.helpers import generate_slug
from services.image_service import save_uploaded_image

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('user_id') or session.get('role') not in ('admin', 'super_admin'):
            abort(404)
        return f(*args, **kwargs)
    return decorated_function

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    stats = EnquiryModel.get_stats()
    products, product_count = ProductModel.find_all(limit=5)
    brands = BrandModel.find_all()
    enquiries, _ = EnquiryModel.find_all(limit=5)
    
    return render_template(
        'admin/dashboard.html',
        stats=stats,
        product_count=product_count,
        brand_count=len(brands),
        recent_products=products,
        recent_enquiries=enquiries
    )

@admin_bp.route('/products')
@admin_required
def products():
    page = int(request.args.get('page', 1))
    business_filter = request.args.get('business', '').strip()
    
    filter_query = {}
    if business_filter:
        filter_query['business_slug'] = business_filter

    products_list, total = ProductModel.find_all(
        filter_query=filter_query, 
        limit=20, 
        page=page, 
        active_only=False
    )
    categories = CategoryModel.find_all()
    from services.category_service import SubcategoryService
    subcategories = SubcategoryService.get_all()
    brands = BrandModel.find_all()
    valid_businesses = [b for b in BUSINESSES if b['slug'] != 'catalogue']
    total_pages = (total + 19) // 20 if total > 0 else 1
    
    return render_template(
        'admin/products.html',
        products=products_list,
        categories=categories,
        subcategories=subcategories,
        brands=brands,
        businesses=valid_businesses,
        current_business=business_filter,
        page=page,
        total_pages=total_pages
    )

@admin_bp.route('/products/create', methods=['POST'])
@admin_required
def create_product():
    data = request.form.to_dict()
    name = data.get('name', '').strip()
    sku = data.get('sku', '').strip()
    
    if not name or not sku:
        flash('Product Name and SKU are required.', 'danger')
        return redirect(url_for('admin.products'))

    # Handle image upload
    image_url = ''
    if 'image' in request.files and request.files['image'].filename:
        file = request.files['image']
        ok, res = save_uploaded_image(file, current_app.config['UPLOAD_FOLDER'], current_app.config['ALLOWED_EXTENSIONS'])
        if ok:
            image_url = res

    # Resolve taxonomy
    business_slug = data.get('business_slug', 'plumbing').strip()
    category_slug = data.get('category_slug', 'pipes').strip()
    subcategory_slug = data.get('subcategory_slug', 'hoses-tubes').strip()
    brand_slug = data.get('brand_slug', 'standard').strip()

    # Look up proper brand name
    brand_name = brand_slug.replace('-', ' ').title()
    for b in BrandModel.find_all():
        if b.get('slug') == brand_slug:
            brand_name = b.get('name', brand_name)
            break

    product_data = {
        'name': name,
        'slug': generate_slug(name),
        'sku': sku.upper(),
        'description': data.get('description', ''),
        'short_description': data.get('short_description', ''),
        'features': [f.strip() for f in data.get('features', '').split('\n') if f.strip()],
        'images': [{'url': image_url or '/static/images/placeholder.jpg', 'is_primary': True}],
        'business_slug': business_slug,
        'category_slug': category_slug,
        'subcategory_slug': subcategory_slug,
        'brand_slug': brand_slug,
        'brand_name': brand_name,
        'is_active': True,
        'is_featured': 'is_featured' in request.form,
        'is_new': 'is_new' in request.form,
    }

    ProductModel.create(product_data)
    flash(f'Product "{name}" added successfully!', 'success')
    return redirect(url_for('admin.products', business=business_slug))

@admin_bp.route('/products/<product_id>/edit', methods=['POST'])
@admin_required
def edit_product(product_id):
    data = request.form.to_dict()
    name = data.get('name', '').strip()
    sku = data.get('sku', '').strip()
    
    if not name or not sku:
        flash('Product Name and SKU are required.', 'danger')
        return redirect(url_for('admin.products'))

    # Retain old image url if none uploaded
    existing = ProductModel.find_by_id(product_id)
    image_url = ''
    if existing and existing.get('images') and len(existing['images']) > 0:
        image_url = existing['images'][0].get('url', '')

    if 'image' in request.files and request.files['image'].filename:
        file = request.files['image']
        ok, res = save_uploaded_image(file, current_app.config['UPLOAD_FOLDER'], current_app.config['ALLOWED_EXTENSIONS'])
        if ok:
            image_url = res

    business_slug = data.get('business_slug', 'plumbing').strip()
    category_slug = data.get('category_slug', 'pipes').strip()
    subcategory_slug = data.get('subcategory_slug', 'hoses-tubes').strip()
    brand_slug = data.get('brand_slug', 'standard').strip()

    # Look up proper brand name
    brand_name = brand_slug.replace('-', ' ').title()
    for b in BrandModel.find_all():
        if b.get('slug') == brand_slug:
            brand_name = b.get('name', brand_name)
            break

    product_data = {
        'name': name,
        'slug': generate_slug(name),
        'sku': sku.upper(),
        'description': data.get('description', ''),
        'short_description': data.get('short_description', ''),
        'features': [f.strip() for f in data.get('features', '').split('\n') if f.strip()],
        'images': [{'url': image_url or '/static/images/placeholder.jpg', 'is_primary': True}],
        'business_slug': business_slug,
        'category_slug': category_slug,
        'subcategory_slug': subcategory_slug,
        'brand_slug': brand_slug,
        'brand_name': brand_name,
        'is_active': 'is_active' in request.form,
        'is_featured': 'is_featured' in request.form,
        'is_new': 'is_new' in request.form,
    }

    success = ProductModel.update(product_id, product_data)
    if success:
        flash(f'Product "{name}" updated successfully!', 'success')
    else:
        flash('Failed to update product.', 'danger')
    return redirect(url_for('admin.products', business=business_slug))

@admin_bp.route('/products/<product_id>/delete', methods=['POST'])
@admin_required
def delete_product(product_id):
    existing = ProductModel.find_by_id(product_id)
    business_slug = existing.get('business_slug', '') if existing else ''
    
    success = ProductModel.delete(product_id)
    if success:
        flash('Product deleted successfully!', 'success')
    else:
        flash('Failed to delete product.', 'danger')
    return redirect(url_for('admin.products', business=business_slug))

@admin_bp.route('/brands')
@admin_required
def brands():
    brands_list = BrandModel.find_all()
    return render_template('admin/brands.html', brands=brands_list, businesses=BUSINESSES)

@admin_bp.route('/enquiries')
@admin_required
def enquiries():
    page = int(request.args.get('page', 1))
    status_filter = request.args.get('status', '')
    enquiry_list, total = EnquiryModel.find_all(status=status_filter or None, page=page, limit=20)
    stats = EnquiryModel.get_stats()
    return render_template('admin/enquiries.html', enquiries=enquiry_list, stats=stats, current_status=status_filter)

@admin_bp.route('/enquiries/<enquiry_id>/status', methods=['POST'])
@admin_required
def update_enquiry_status(enquiry_id):
    status = request.form.get('status', 'read')
    notes = request.form.get('notes', '')
    EnquiryModel.update_status(enquiry_id, status, notes)
    flash('Enquiry status updated.', 'success')
    return redirect(url_for('admin.enquiries'))

@admin_bp.route('/settings', methods=['GET', 'POST'])
@admin_required
def settings():
    if request.method == 'POST':
        for key, value in request.form.items():
            SettingModel.set_value(key, value)
        flash('Settings updated successfully.', 'success')
        return redirect(url_for('admin.settings'))

    all_settings = SettingModel.get_all()
    return render_template('admin/settings.html', settings=all_settings)
