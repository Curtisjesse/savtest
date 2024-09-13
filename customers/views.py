from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.permissions import AllowAny

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer