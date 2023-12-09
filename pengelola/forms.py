from django.forms import ModelForm
from pengelola.models import Buku
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormBuku(ModelForm):
    class Meta:
        model = Buku
        fields = ["title","language","first_name",
                  "last_name","year","subjects", "bookshelves"]

class FormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'is_staff', )
