from flask import Blueprint, jsonify

order_bp = Blueprint('order', __name__, url_prefix='/orders')

@order_bp.route('/')
def list_orders():
    return jsonify({'success': False, 'message': 'E-commerce orders feature is scaffolded for future release.'}), 400
