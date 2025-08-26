from django.db import models
# from User.models import Customer

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
    sales_price = models.DecimalField(decimal_places=2, max_digits=9)
    Quantity = models.IntegerField()
    decription = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.image if self.image else "No Image"}'

class Review(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
        user = models.ForeignKey(Customer, on_delete=models.CASCADE)
        rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)]) 
        comment = models.TextField(blank=True, null=True)
        created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    pass