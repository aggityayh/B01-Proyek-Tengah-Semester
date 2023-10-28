from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Ulasan
from .forms import ReviewForm
from pengelola.models import Buku
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url='/login/')
def show_ulasan(request):
    books = Buku.objects.all()

    context = {
        'name': 'AncestralReads',
        'books': books
    }

    return render(request, "ulasan.html", context)

@csrf_exempt
def add_review_ajax(request):
    if request.method == 'POST':
        reviewer_name = request.POST.get("reviewer_name")
        review_text = request.POST.get("review_text")
        rating = request.POST.get("rating")
        user = request.user
        buku_id = request.POST.get("buku") 
        book_temp = Buku.objects.get(pk=buku_id)

        ulasan = Ulasan(buku=book_temp, reviewer_name=reviewer_name, review_text=review_text, rating=rating, user=user)
        ulasan.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_ulasan_json(request):
    review = Ulasan.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', review))



