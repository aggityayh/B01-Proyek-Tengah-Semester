from django import forms
from pengelola.models import Buku
from booklist.models import Book

class addBook_form(forms.Form):
    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request', None)
        super(addBook_form, self).__init__(*args, **kwargs)
        title_list = Book.objects.filter(user=request.user)
        if title_list:
            title_list = title_list.values_list('title', flat=True)
            Bukus = Buku.objects.exclude(title__in=title_list)
        else:
            Bukus = Buku.objects.all()
        field_buku = ((None, 'Select...'),)
        for book in Bukus:
            field_buku += ((book.pk, book.title),)
        self.fields['addBook_field'] = forms.ChoiceField(
            label="Options",
            widget=forms.Select(attrs={'class': 'custom-select'}),
            choices = field_buku,
        )