from flask import Blueprint, render_template, request, jsonify
from services.enquiry_service import EnquiryService
from services.email_service import send_enquiry_email
from utils.constants import COMPANY_INFO

enquiry_bp = Blueprint('enquiry', __name__)

@enquiry_bp.route('/contact')
def contact():
    return render_template('contact.html', company=COMPANY_INFO)

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

            return jsonify({
                "success": True,
                "message": "Thank you! Our team will contact you shortly."
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
