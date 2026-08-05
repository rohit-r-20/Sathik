import re

def validate_enquiry_input(data):
    """
    Validates enquiry/contact form fields.
    Returns (is_valid, errors_dict)
    """
    errors = {}
    name = (data.get('name') or '').strip()
    phone = (data.get('phone') or '').strip()
    email = (data.get('email') or '').strip()
    city = (data.get('city') or '').strip()
    message = (data.get('message') or '').strip()

    if not name or len(name) < 2:
        errors['name'] = 'Name must be at least 2 characters'
    
    if not phone or not re.match(r'^[6-9]\d{9}$', phone):
        errors['phone'] = 'Enter a valid 10-digit Indian mobile number'

    if not email or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        errors['email'] = 'Enter a valid email address'

    if not city or len(city) < 2:
        errors['city'] = 'City must be at least 2 characters'

    if not message or len(message) < 5:
        errors['message'] = 'Message must be at least 5 characters'

    return len(errors) == 0, errors

def validate_login_input(email, password):
    """
    Validates login input credentials.
    """
    errors = {}
    if not email or '@' not in email:
        errors['email'] = 'Enter a valid email address'
    if not password or len(password) < 4:
        errors['password'] = 'Password is required'
    return len(errors) == 0, errors
