from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Customer

class CustomerTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {'name': 'Curtis Jesse', 'code': 'CJ001', 'phone_number': '+254741594863'}
        self.response = self.client.post(
            reverse('customer-list'),
            self.customer_data,
            format="json")

    def test_create_customer(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().name, 'Curtis Jesse')

    def test_get_customer(self):
        customer = Customer.objects.get()
        response = self.client.get(
            reverse('customer-detail', kwargs={'pk': customer.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Curtis Jesse')