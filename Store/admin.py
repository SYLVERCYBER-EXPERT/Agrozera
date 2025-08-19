from django.contrib import admin
# Importing Store App models 
from Store.models import Category, Product

# Register Category models 
admin.site.register(Category)

# Register Product models
admin.site.register(Product)
