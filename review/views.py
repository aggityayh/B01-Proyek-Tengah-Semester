import json
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import get_object_or_404, render
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
    ulasan = Ulasan.objects.filter(user=request.user)
    books = Buku.objects.all()
    #buku=Buku.objects.get(pk=)

    context = {
        'name': 'AncestralReads',
        'ulasan': ulasan,
        'books' : books,
        'nama' : request.user.username,
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
        #book_title = book_temp.fields.title
        
        ulasan = Ulasan(buku=book_temp, reviewer_name=reviewer_name, review_text=review_text, rating=rating, user=user)
        ulasan.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_ulasan_json(request):
    review = Ulasan.objects.filter(user=request.user).values('pk', 'buku__title', 'reviewer_name', 'review_text', 'rating', 'review_date','user')
    return JsonResponse(list(review), safe=False)


@csrf_exempt
def delete_ajax(request):
    if request.method == "DELETE":
        try:
            id = json.loads(request.body.decode('utf-8')).get('pk')
            book_temp = Ulasan.objects.get(pk=id)
            book_temp.delete()
            
            return HttpResponse(b"DELETED", status=201)
        except:
            return HttpResponse(b"Not Found", status=201)

    return HttpResponseNotFound()

def show_json(request):
    data = Ulasan.objects.filter(user=request.user)
    #print(data.values)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# def get_book_json(request):
#     book_item = Book.objects.filter(user=request.user)
#     return HttpResponse(serializers.serialize('json', book_item))

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Ulasan.objects.create(
            user = request.user,
            nama = data["reviewer_name"],
            rating = int(data["rating"]),
            deskripsi = data["review_text"],
            buku = get_object_or_404(Buku, pk = data["id_buku"])
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)




