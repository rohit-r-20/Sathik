def process_payment_stub(order_id, amount, payment_method):
    """
    Future payment gateway processing stub (Razorpay / Stripe / PhonePe).
    Currently unreferenced in product catalogue mode.
    """
    return {
        'status': 'initiated',
        'order_id': order_id,
        'amount': amount,
        'payment_method': payment_method,
        'message': 'Payment gateway processing stub'
    }
