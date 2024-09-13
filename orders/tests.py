from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order
from customers.models import Customer

class OrderTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer = Customer.objects.create(name='Curtis Jesse', code='CJ001', phone_number='+254741594863')
        self.order_data = {'customer': self.customer.id, 'item': 'Test Item', 'amount': '100.00'}
        self.response = self.client.post(
            reverse('order-list'),
            self.order_data,
            format="json")

    def test_create_order(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().item, 'Test Item')

    def test_get_order(self):
        order = Order.objects.get()
        response = self.client.get(
            reverse('order-detail', kwargs={'pk': order.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['item'], 'Test Item')