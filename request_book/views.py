from django.shortcuts import render

from request_book.models import Product
from request_book.forms import ProductForm
import json
from django.http import *
from django.urls import reverse

from pengelola.models import Buku

from django.http import HttpResponse
from django.core import serializers

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  

from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import get_object_or_404

from django.views.decorators.csrf import csrf_exempt

def show_main(request):
    products = Product.objects.filter(user=request.user)
    books = Buku.objects.exclude(title__in=products)
    total_items = products.count()

    context = {
        'name': request.user.username,
        'class': 'PBP B',
        'products': products,
        'books': books,
        'total_items': total_items,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "request_book.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.amount = 0
        product.save()
        return HttpResponseRedirect(reverse('request_book:show_main'))

    context = {'form': form}
    return render(request, "create_req.html", context)

def increase_amount(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.amount += 1
    product.save()
    return HttpResponseRedirect(reverse('request_book:show_main'))

def decrease_amount(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Mengurangi jumlah barang sebanyak satu jika barang ada 
    if product.amount > 0:
        product.amount -= 1
        product.save()
        
    # Jika jumlah mencapai 0, product akan dihapus dari keranjang
    if product.amount == 0:
        product.delete()
    
    return HttpResponseRedirect(reverse('request_book:show_main'))

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    return HttpResponseRedirect(reverse('request_book:show_main'))

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('request_book:show_main'))

    context = {'form': form}
    return render(request, "edit_req.html", context)

@csrf_exempt
def add_product_ajax(request):
    print(request.POST)
    if request.method == 'POST':

        title = request.POST.get("title")
        if Buku.objects.filter(title=title).exists():
            return HttpResponse(b"DUPLICATE", status=201)

        language = request.POST.get("language")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        year = request.POST.get("year")
        subjects = request.POST.get("subjects")
        user = request.user
        amount = 0

        new_product = Product(title=title, language=language, first_name=first_name, last_name=last_name, year=year, subjects=subjects, user=user, amount=amount)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

@csrf_exempt
def add_product_flutter(request):
    print(request.POST)
    if request.method == 'POST':

        title = request.POST.get("title")
        if Buku.objects.filter(title=title).exists():
            return JsonResponse(b"DUPLICATE", status=401)

        language = request.POST.get("language")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        year = request.POST.get("year")
        subjects = request.POST.get("subjects")
        user = request.user
        amount = 0

        new_product = Product(title=title, language=language, first_name=first_name, last_name=last_name, year=year, subjects=subjects, user=user, amount=amount)
        new_product.save()

        return JsonResponse(b"CREATED", status=201)

def delete_product_flutter(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    # Mengurangi jumlah barang sebanyak satu jika barang ada 
    if product.amount > 0:
        product.amount -= 1
        product.save()
        
    # Jika jumlah mencapai 0, product akan dihapus dari keranjang
    if product.amount == 0:
        product.delete()
    
    return JsonResponse({"status": "success"}, status=200)

@csrf_exempt
def delete_product_ajax(request, id):
    if request.method == 'DELETE':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return HttpResponse(b"DELETED", status=204)
    return HttpResponseNotFound()

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")