from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from pengelola.models import Buku
from pengelola.forms import FormBuku
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.core import serializers
from django.urls import reverse
import datetime

@login_required(login_url='/login/')
def show_main(request):
    buku = Buku.objects.all()
    if request.user.is_staff == True:
        status = "Pustakawan"
        site = "kelola.html"
    else:
        status = "Pengguna"
        site = "main.html"

    context = {
        'username' : request.user.username,
        'status' : status,
        'buku' : buku,
        'last_login' : request.COOKIES['last_login'],
    }
    return render(request, site, context)

def get_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def display_books(request):
    data = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", data))


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if "pustakawan" in request.POST:
                messages.success(request, 'Welcome new staff!')
                user.is_staff = True
                return redirect('pengelola:login')
            messages.success(request, 'Your account has been successfully created!')
            return redirect('pengelola:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("pengelola:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('pengelola:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
def tambah_buku(request):
    if request.method == 'POST':
        text_number = request.POST.get("text_number")
        title = request.POST.get("title")
        language = request.POST.get("language")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        year = request.POST.get('year')
        subjects = request.POST.get('subjects')
        bookshelves = request.POST.get('bookshelves')

        new_book = Buku(text_number=text_number, title=title, language=language, first_name=first_name, 
                        last_name=last_name, year=year, subjects=subjects, bookshelves=bookshelves)
        new_book.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()

def hapus_buku(request, id):
    buku = Buku.objects.get(pk = id)
    buku.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def edit_buku(request, id):
    Buku = Buku.objects.get(pk = id)
    form = FormBuku(request.POST or None, instance=Buku)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)