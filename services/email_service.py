import os
import resend
from dotenv import load_dotenv

load_dotenv()

def send_enquiry_email(enquiry):
    """
    Sends a formatted email notification for new customer enquiries using the official Resend Python SDK.
    Catches any exceptions and logs them without breaking enquiry submission.
    """
    api_key = os.getenv('RESEND_API_KEY')
    from_email = os.getenv('RESEND_FROM', 'onboarding@resend.dev')
    to_email = os.getenv('RESEND_TO', 'vrrohit2020@gmail.com')

    if not api_key:
        print("⚠️ Resend Notice: RESEND_API_KEY environment variable is missing. Email notification skipped.")
        return False

    resend.api_key = api_key

    customer_name = enquiry.get('customer_name') or enquiry.get('name') or 'N/A'
    mobile_number = enquiry.get('mobile_number') or enquiry.get('mobile') or enquiry.get('phone') or 'N/A'
    email = enquiry.get('email') or 'N/A'
    address = enquiry.get('address') or enquiry.get('city') or 'N/A'
    interested_in = enquiry.get('interested_in') or enquiry.get('category') or 'N/A'
    product_name = enquiry.get('product_name') or 'N/A'
    preferred_contact = enquiry.get('preferred_contact') or 'WhatsApp Message'
    message = enquiry.get('message') or 'N/A'
    page_url = enquiry.get('page_url') or 'N/A'
    status = enquiry.get('status') or 'New'

    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{ font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f8fafc; color: #0f172a; margin: 0; padding: 20px; }}
        .card {{ max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 8px; border: 1px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 12px rgba(15,23,42,0.05); }}
        .header {{ background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 24px; text-align: center; }}
        .header h2 {{ margin: 0; font-size: 20px; letter-spacing: 0.05em; text-transform: uppercase; color: #f97316; }}
        .header p {{ margin: 6px 0 0; font-size: 13px; color: #94a3b8; }}
        .content {{ padding: 24px; }}
        .table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
        .table td {{ padding: 10px 12px; border-bottom: 1px solid #f1f5f9; font-size: 14px; vertical-align: top; }}
        .table td.label {{ font-weight: 700; color: #475569; width: 35%; background-color: #f8fafc; }}
        .table td.value {{ color: #0f172a; font-weight: 500; }}
        .footer {{ background-color: #f8fafc; border-top: 1px solid #e2e8f0; padding: 16px; text-align: center; font-size: 12px; color: #64748b; }}
        .status-tag {{ display: inline-block; background-color: #ffedd5; color: #c2410c; padding: 2px 8px; border-radius: 4px; font-weight: 700; font-size: 12px; }}
      </style>
    </head>
    <body>
      <div class="card">
        <div class="header">
          <h2>Sathik Groups</h2>
          <p>🔔 New B2B Enquiry Received</p>
        </div>
        <div class="content">
          <table class="table">
            <tr><td class="label">Customer Name</td><td class="value"><strong>{customer_name}</strong></td></tr>
            <tr><td class="label">Mobile Number</td><td class="value"><a href="tel:{mobile_number}" style="color: #c2410c; font-weight: 700;">{mobile_number}</a></td></tr>
            <tr><td class="label">Email Address</td><td class="value">{email}</td></tr>
            <tr><td class="label">Address / Location</td><td class="value">{address}</td></tr>
            <tr><td class="label">Interested In</td><td class="value">{interested_in}</td></tr>
            <tr><td class="label">Product Name</td><td class="value">{product_name}</td></tr>
            <tr><td class="label">Preferred Contact</td><td class="value">{preferred_contact}</td></tr>
            <tr><td class="label">Additional Message</td><td class="value">{message}</td></tr>
            <tr><td class="label">Submitted From Page</td><td class="value"><a href="{page_url}" style="color: #475569;">{page_url}</a></td></tr>
            <tr><td class="label">Status</td><td class="value"><span class="status-tag">{status}</span></td></tr>
          </table>
        </div>
        <div class="footer">
          <p>This is an automated notification from Sathik Groups Commercial Product Catalogue Platform.</p>
        </div>
      </div>
    </body>
    </html>
    """

    params: resend.Emails.SendParams = {
        "from": from_email,
        "to": [to_email],
        "subject": "🔔 New Enquiry - Sathik Groups",
        "html": html_content
    }

    try:
        response = resend.Emails.send(params)
        print(f"✅ Resend email sent successfully! Response: {response}")
        return True
    except Exception as e:
        print(f"⚠️ Resend Email Error (Preserving submission): {e}")
        # Testing mode fallback if testing email restricted to account email
        if "only send testing emails to your own email address" in str(e).lower():
            try:
                fallback_params: resend.Emails.SendParams = {
                    "from": from_email,
                    "to": ["andersonjuds01@gmail.com"],
                    "subject": "🔔 New Enquiry - Sathik Groups",
                    "html": html_content
                }
                fb_res = resend.Emails.send(fallback_params)
                print(f"✅ Resend email sent to account owner email! Response: {fb_res}")
                return True
            except Exception as fb_err:
                print(f"⚠️ Resend fallback error: {fb_err}")
        return False
