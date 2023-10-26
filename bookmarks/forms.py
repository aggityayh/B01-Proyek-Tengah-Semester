from django.forms import ModelForm
from bookmarks.models import Book

class ProductForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "year"]