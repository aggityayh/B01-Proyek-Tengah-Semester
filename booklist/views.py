from django.shortcuts import render
from booklist.models import Book
from booklist.forms import addBook_form
from pengelola.models import Buku
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

# Create your views here.

def show_booklist(request):
    title_list = Book.objects.values_list('title', flat=True)
    books = Buku.objects.exclude(title__in=title_list)
    try:
        user = request.user
    except:
        user = None

    context = {
        'nameapp': 'BookList',
        'user': user,
        'books': books,
        'form': addBook_form(request=request)
    }
    return render(request, "booklist.html", context)

def get_book_json(request):
    book_item = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', book_item))

def get_buku_json(request):
    title_list = Book.objects.filter(user=request.user).values_list('title', flat=True)
    buku_item = Buku.objects.exclude(title__in=title_list)
    return HttpResponse(serializers.serialize('json', buku_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        book_temp = Buku.objects.get(pk=request.POST.get("addBook_field"))
        title_list = Book.objects.filter(user=request.user).values_list('title', flat=True)
        if book_temp.title in title_list:
            return HttpResponse(b"DUPLICATE", status=201)
        new_book = Book(text_number=book_temp.text_number, title=book_temp.title, language=book_temp.language, first_name=book_temp.first_name, last_name=book_temp.last_name, year=book_temp.year, subjects=book_temp.subjects, bookshelves=book_temp.bookshelves, user=request.user)
        new_book.save()
        
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_book_ajax(request):
    if request.method == "DELETE":
        try:
            id = json.loads(request.body.decode('utf-8')).get('pk')
            book_temp = Book.objects.filter(user=request.user).get(pk=id)
            book_temp.delete()
            
            return HttpResponse(b"DELETED", status=201)
        except:
            return HttpResponse(b"Not Found", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_book_flutter(request):
    if request.method == "POST":
        try:
            id = json.loads(request.body.decode('utf-8')).get('pk')
            book_temp = Book.objects.filter(user=request.user).get(pk=id, user=request.user)
            book_temp.delete()
            return JsonResponse({"status": "success"}, status=200)
        except:
            return JsonResponse({"status": "not found"}, status=200)
    return JsonResponse({"status": "error"}, status=401)