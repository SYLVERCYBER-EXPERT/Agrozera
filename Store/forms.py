from django import forms
from Store.models import Product, Review


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {'rating': forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)]),}

