import os
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "savtest.settings")
django.setup()

import africastalking

# Initialize Africa's Talking with credentials from environment variables
username = settings.AFRICASTALKING_USERNAME
api_key = settings.AFRICASTALKING_API_KEY

print(f"Using username: {username}")
print(f"API key (first 5 chars): {api_key[:5]}...")

africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_test_sms(phone_number):
    try:
        message = "This is a test SMS from your Django app"
        response = sms.send(message, [phone_number])
        print(f"Message sent successfully. Response: {response}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

if __name__ == "__main__":
    test_phone_number = "+254741594863"
    print(f"Sending test SMS to {test_phone_number}...")
    send_test_sms(test_phone_number)
    print("Test completed.")