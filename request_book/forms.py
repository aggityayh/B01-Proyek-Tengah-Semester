from django.forms import ModelForm
from request_book.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "language", "first_name", "last_name", "year", "subjects"]