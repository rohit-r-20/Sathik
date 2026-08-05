from flask import Blueprint, jsonify

payment_bp = Blueprint('payment', __name__, url_prefix='/payment')

@payment_bp.route('/checkout', methods=['POST'])
def checkout():
    return jsonify({'success': False, 'message': 'Online payments are currently disabled. Please use Request Quote or WhatsApp to enquire.'}), 400
