from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, jsonify, current_app
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
        if not session.get('user_id'):
            flash('Please sign in to access the admin portal.', 'warning')
            return redirect(url_for('auth.login'))
        if session.get('role') not in ('admin', 'super_admin'):
            flash('Admin access required.', 'danger')
            return redirect(url_for('home.index'))
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
    products_list, total = ProductModel.find_all(limit=20, page=page)
    categories = CategoryModel.find_all()
    brands = BrandModel.find_all()
    total_pages = (total + 19) // 20 if total > 0 else 1
    
    return render_template(
        'admin/products.html',
        products=products_list,
        categories=categories,
        brands=brands,
        businesses=BUSINESSES,
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
    if 'image' in request.files:
        file = request.files['image']
        ok, res = save_uploaded_image(file, current_app.config['UPLOAD_FOLDER'], current_app.config['ALLOWED_EXTENSIONS'])
        if ok:
            image_url = res

    # Resolve taxonomy
    business_slug = data.get('business_slug', 'plumbing')
    category_slug = data.get('category_slug', 'pipes')
    subcategory_slug = data.get('subcategory_slug', 'cpvc-pipes')
    brand_slug = data.get('brand_slug', 'astral')

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
        'brand_name': brand_slug.title(),
        'is_active': True,
        'is_featured': 'is_featured' in request.form,
        'is_new': 'is_new' in request.form,
    }

    ProductModel.create(product_data)
    flash('Product created successfully!', 'success')
    return redirect(url_for('admin.products'))

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
