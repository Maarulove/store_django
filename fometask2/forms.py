from django import forms
from .models import Goods


class ProductForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['name', "description", 'price', 'photo', "amount"]

        
        widgets = {
            "date_publish": forms.DateInput(attrs={"class": "form-control", "type":'date'}),
        }
