from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from pengelola.models import Buku
from pengelola.forms import FormBuku, FormUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, JsonResponse
from django.core import serializers
from django.urls import reverse
import datetime
import json

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
    form = FormUser()

    if request.method == "POST":
        form = FormUser(request.POST)
        print(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_staff == True:
                messages.success(request, 'Welcome new staff!')   
                return redirect('pengelola:login')
            messages.success(request, 'Your account has been successfully created!')
            return redirect('pengelola:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    next_url = request.GET.get('next', None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                response = HttpResponseRedirect(next_url)
            else:
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

@csrf_exempt
def edit_buku(request, id):
    buku = get_object_or_404(Buku, text_number = id)
    if request.method == 'POST' :
        buku.title = request.POST.get("title2")
        buku.language = request.POST.get("language2")
        buku.first_name = request.POST.get('first_name2')
        buku.last_name = request.POST.get('last_name2')
        buku.year = request.POST.get('year2')
        buku.subjects = request.POST.get('subjects2')
        buku.bookshelves = request.POST.get('bookshelves2')
        buku.save()

        return HttpResponse(b"UPDATED", status=202)
    return HttpResponseNotFound()

@csrf_exempt
def edit_buku_flutter(request, id):
    buku = get_object_or_404(Buku, pk = id)
    if request.method == 'POST' :
        data = json.loads(request.body)
        buku.text_number = int(data["text_number"]),
        buku.title = data["title"],
        buku.language = data["language"],
        buku.first_name = data["first_name"],
        buku.last_name = data["last_name"],
        buku.year = data["year"],
        buku.subjects = data["subjects"],
        buku.bookshelves = data["bookshelves"]
        buku.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def hapus_buku_flutter(request, id):
    buku = get_object_or_404(Buku, text_number = id)
    buku.delete()
    return JsonResponse({"status": "success"}, status=200)

@csrf_exempt
def create_buku_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_book = Buku.objects.create(
            text_number = int(data["text_number"]),
            title = data["title"],
            language = data["language"],
            first_name = data["first_name"],
            last_name = data["last_name"],
            year = data["year"],
            subjects = data["subjects"],
            bookshelves = data["bookshelves"]
        )

        new_book.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)


@csrf_exempt
def hapus_buku(request, id):
    buku = get_object_or_404(Buku, text_number = id)
    buku.delete()
    return HttpResponse(b"DELETED", status=202)

@csrf_exempt
def emergency_hapus_buku(request, id):
    buku = get_object_or_404(Buku, pk = id)
    buku.delete()
    return HttpResponse(b"DELETED", status=202)
