from django.forms import ModelForm
from request_book.models import Book

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ["title", "language", "first_name", "last_name", "year", "subjects"]