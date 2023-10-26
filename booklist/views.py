from django.shortcuts import render
from booklist.models import Book
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def show_booklist(request):
    books = Book.objects.all()

    context = {
        'nameapp': 'AncestralReads',
        'books': books
    }
    return render(request, "booklist.html", context)

def get_book_json(request):
    book_item = Book.objects.all()
    return HttpResponse(serializers.serialize('json', book_item))

@csrf_exempt
def add_book_ajax(request):
    if request.method == 'POST':
        book_temp = Book.objects.get(pk=request.POST.get("buku"))
        new_book = Book(text_number=book_temp.text_number, title=book_temp.title, language=book_temp.language, first_name=book_temp.first_name, last_name=book_temp.last_name, year=book_temp.year, subjects=book_temp.subjects, bookshelves=book_temp.bookshelves)
        new_book.save()
        
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()