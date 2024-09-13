import africastalking
from django.conf import settings
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Initialize Africa's Talking
africastalking.initialize(
    username=settings.AFRICASTALKING_USERNAME,
    api_key=settings.AFRICASTALKING_API_KEY
)
sms = africastalking.SMS

def send_order_notification(phone_number, order):
    """
    Send an SMS notification about a new order.
    """
    message = f"New order placed: {order.item} for ${order.amount}"
    logger.info(f"Attempting to send SMS to {phone_number}: {message}")
    try:
        response = sms.send(message, [phone_number])
        logger.info(f"SMS sent successfully: {response}")
        return True
    except Exception as e:
        logger.error(f"Error sending SMS: {e}")
        return False