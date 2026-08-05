from flask import Blueprint, jsonify, render_template
from models.category import CategoryModel, SubcategoryModel

category_bp = Blueprint('category', __name__)

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
