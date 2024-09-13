from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Order
from .serializers import OrderSerializer
from .sms_service import send_order_notification
import logging

logger = logging.getLogger(__name__)

class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        logger.info(f"Order created for customer: {customer.name}")
        if customer.phone_number:
            logger.info(f"Sending SMS to {customer.phone_number}")
            success = send_order_notification(customer.phone_number, order)
            if success:
                logger.info("SMS sent successfully")
            else:
                logger.error("Failed to send SMS")
        else:
            logger.warning(f"No phone number for customer: {customer.name}")