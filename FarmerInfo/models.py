from django.db import models

# Farmer information
class FarmerData(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class FarmSupply(models.Model):
    farmer_name = models.ForeignKey('first_name' + 'last_name', on_delete = models.CASCADE)
    farm_product = models.CharField(max_length=200)
    farm_location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.farmer_name} {self.farm_product} {self.farm_location}'