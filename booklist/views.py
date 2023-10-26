from django.shortcuts import render
from booklist.models import Book
from pengelola.models import Buku
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='pengelola/login/')
def show_booklist(request):
    books = Buku.objects.all()

    context = {
        'nameapp': 'AncestralReads',
        'books': books
    }
    return render(request, "booklist.html", context)

def get_book_json(request):
    book_item = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', book_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        book_temp = Buku.objects.get(pk=request.POST.get("buku"))
        new_book = Book(text_number=book_temp.text_number, title=book_temp.title, language=book_temp.language, first_name=book_temp.first_name, last_name=book_temp.last_name, year=book_temp.year, subjects=book_temp.subjects, bookshelves=book_temp.bookshelves, user=request.user)
        new_book.save()
        
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()