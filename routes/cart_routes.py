from flask import Blueprint, jsonify, session
from models.cart import CartModel

cart_bp = Blueprint('cart', __name__, url_prefix='/cart')

@cart_bp.route('/')
def view_cart():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'success': False, 'message': 'Authentication required'}), 401
    cart = CartModel.get_user_cart(user_id)
    return jsonify({'success': True, 'data': cart or {'items': []}})

@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    # Scaffolded for future e-commerce expansion
    return jsonify({'success': False, 'message': 'E-commerce cart is not currently active on this product catalogue.'}), 400
