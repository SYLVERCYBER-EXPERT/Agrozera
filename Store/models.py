from django.db import models


#Product Category
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return f'{self.name}'

# Product Model
class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=9, default=1, null=False)
    decription = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.image if self.image else "No Image"}'

