from django.db import models
# import Product from store app
from Store.models import Product

# Farmer information
class FarmerData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    profile_picture = models.ImageField(upload_to='FarmerProfile/')
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    date_registered = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.city}'


class FarmSupply(models.Model):
    farmer = models.ForeignKey(FarmerData, on_delete = models.CASCADE)
    products = models.ManyToManyField(Product)
    farm_location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.farmer.first_name} {self.farmer.last_name} {self.farm_location}'