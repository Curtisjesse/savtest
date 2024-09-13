from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True) 

    def __str__(self):
        return self.name