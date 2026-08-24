from flask import Blueprint, render_template, redirect, url_for
from models.product import ProductModel
from models.brand import BrandModel
from models.project import ProjectModel
from utils.constants import BUSINESSES, COMPANY_INFO

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    featured_products = ProductModel.find_featured(limit=8)
    featured_brands = BrandModel.find_all(featured_only=True)
    return render_template(
        'index.html',
        businesses=BUSINESSES,
        featured_products=featured_products,
        featured_brands=featured_brands,
        company=COMPANY_INFO
    )

@home_bp.route('/about')
def about():
    return redirect(url_for('home.index') + '#aboutUs')

@home_bp.route('/projects')
def projects():
    project_list = ProjectModel.find_all()
    return render_template('projects.html', projects=project_list, company=COMPANY_INFO)
