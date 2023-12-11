from django.forms import ModelForm
from pengelola.models import Buku

class ProductForm(ModelForm):
    class Meta:
        model = Buku
        fields = ["title","language","first_name",
                  "last_name","year","subjects", "bookshelves"]