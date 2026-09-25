from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.enquiry_service import EnquiryService
from services.email_service import send_enquiry_email
from services.whatsapp_service import process_whatsapp_enquiry
from utils.constants import COMPANY_INFO

enquiry_bp = Blueprint('enquiry', __name__)

@enquiry_bp.route('/contact')
def contact():
    return redirect(url_for('home.index') + '#contactUs')

@enquiry_bp.route('/enquiry/submit', methods=['POST'])
def submit_enquiry():
    data = request.form.to_dict() if request.form else (request.get_json() or {})

    # Extract customer input fields with support for both form field naming conventions
    customer_name = (data.get('customer_name') or data.get('name') or '').strip()
    mobile_number = (data.get('mobile_number') or data.get('phone') or '').strip()
    email = (data.get('email') or '').strip()
    address = (data.get('address') or data.get('city') or '').strip()
    interested_in = (data.get('interested_in') or data.get('category') or data.get('business_slug') or '').strip()
    product_name = (data.get('product_name') or '').strip()
    preferred_contact = (data.get('preferred_contact') or 'WhatsApp Message').strip()
    message = (data.get('message') or '').strip()
    page_url = (request.referrer or data.get('page_url') or '').strip()

    # Validation: Customer Name & Mobile Number are required
    if not customer_name or not mobile_number:
        return jsonify({
            "success": False,
            "message": "Unable to save enquiry."
        }), 400

    enquiry_data = {
        'customer_name': customer_name,
        'mobile_number': mobile_number,
        'email': email,
        'address': address,
        'interested_in': interested_in,
        'product_name': product_name,
        'preferred_contact': preferred_contact,
        'message': message,
        'page_url': page_url,
        'status': 'New'
    }

    try:
        success = EnquiryService.create_enquiry(enquiry_data)
        if success:
            # Send Resend email notification (non-blocking if it fails)
            try:
                send_enquiry_email(enquiry_data)
            except Exception as mail_err:
                print(f"⚠️ Email notification trigger notice: {mail_err}")

            # WhatsApp Automation Trigger & URL generation
            whatsapp_info = {}
            try:
                whatsapp_info = process_whatsapp_enquiry(enquiry_data)
            except Exception as wa_err:
                print(f"⚠️ WhatsApp processing notice: {wa_err}")

            # Record quotation so it appears in the Admin Quotation section
            try:
                from models.quotation import QuotationModel
                quote_payload = {
                    'customer_name': customer_name,
                    'mobile_number': mobile_number,
                    'email': email,
                    'city': address,
                    'address': address,
                    'interested_in': interested_in,
                    'product_name': product_name,
                    'product_sku': data.get('product_sku') or data.get('sku') or '',
                    'quantity': data.get('quantity') or data.get('qty') or '',
                    'preferred_contact': preferred_contact,
                    'message': message,
                    'type': data.get('type') or 'quote',
                    'items_json': data.get('items_json') or '',
                    'whatsapp_url': whatsapp_info.get("whatsapp_url") or ''
                }
                quote_record = QuotationModel.create(quote_payload)
            except Exception as quote_err:
                print(f"⚠️ Quotation recording notice: {quote_err}")
                quote_record = None

            return jsonify({
                "success": True,
                "message": "Thank you! Your quote request has been received.",
                "whatsapp_url": whatsapp_info.get("whatsapp_url"),
                "target_phone": whatsapp_info.get("target_phone"),
                "quotation_id": quote_record.get("id") if quote_record else None,
                "quotation_reference": quote_record.get("reference_id") if quote_record else None
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": "Unable to save enquiry."
            }), 500
    except Exception as e:
        print(f"Error handling enquiry submit route: {e}")
        return jsonify({
            "success": False,
            "message": "Unable to save enquiry."
        }), 500

@enquiry_bp.route('/quotations/record-click', methods=['POST'])
def record_quotation_click():
    try:
        data = request.get_json(silent=True) if request.is_json else request.form.to_dict()
        if not data:
            data = {}
        from models.quotation import QuotationModel
        quote_payload = {
            'customer_name': data.get('name') or data.get('customer_name') or 'Direct WhatsApp Visitor',
            'mobile_number': data.get('phone') or data.get('mobile_number') or '',
            'city': data.get('city') or '',
            'product_name': data.get('product_name') or 'Product Enquiry',
            'product_sku': data.get('sku') or data.get('product_sku') or '',
            'message': data.get('message') or 'Clicked Direct WhatsApp Enquiry button on product page',
            'type': 'direct_whatsapp',
            'whatsapp_url': data.get('whatsapp_url') or ''
        }
        record = QuotationModel.create(quote_payload)
        return jsonify({
            'ok': True,
            'success': True,
            'quotation_id': record['id'] if record else None,
            'quotation_reference': record['reference_id'] if record else None
        }), 200
    except Exception as e:
        return jsonify({'ok': False, 'success': False, 'error': str(e)}), 500
