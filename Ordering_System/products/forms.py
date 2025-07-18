from django import forms
from .models import Product

##auto fill , compay, user, timestamp
##so company actually has to fill name, price, stock
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock']  
        ##created_by is username of authenticated user
        ##created_at immutable auto_now
        ##last_updated_at  mutable auto_now
        ##is_active true by default