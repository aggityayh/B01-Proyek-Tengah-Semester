from django.shortcuts import render

from request_book.models import Book
from request_book.forms import BookForm

from django.http import *
from django.urls import reverse

from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

def show_request_book(request):
    books = Book.objects.filter(user=request.user)

    context = {
        'books': books,
    }

    return render(request, "request_book.html", context)

@csrf_exempt
def create_request_ajax(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        language = request.POST.get("language")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        year = request.POST.get("year")
        subjects = request.POST.get("subjects")

        new_book = Book(title=title, language=language, first_name=first_name, last_name=last_name, year=year, subjects=subjects)
        new_book.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def show_xml(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Book.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Book.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def get_book_json(request):
    product_item = Book.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))