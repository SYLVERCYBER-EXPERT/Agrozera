from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, unique=True)
    street_address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.city}'
