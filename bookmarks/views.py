from django.http import HttpResponse
from django.http import HttpResponseRedirect
from bookmarks.forms import ProductForm
from django.shortcuts import redirect, render
from django.urls import reverse
from bookmarks.models import Book
from bookmarks.models import Bookmark
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required(login_url='/login')
def show_main(request):
    # books = Book.objects.filter(book=request.book)
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        form.save()
        return HttpResponseRedirect(reverse('bookmarks:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def add_bookmark(request,id):
    if request.method == "POST":
        book = Book.objects.get(pk=id)
        # user = request.user
        bookmark = Bookmark(title=book.title, year=book.year)
        bookmark.save()
        # bookmark, created = Bookmark.objects.get_or_create(user=user, title=book.title, year=book.year)
        # if created:
        #     bookmark.save()
        
        
    # return HttpResponseRedirect(reverse('bookmarks:show_main'))
    return redirect('bookmarks:show_main')
    
    
def show_bookmarks(request):
    bookmarks = Bookmark.objects.all()
    # user = request.user
    context = {
        'bookmarks': bookmarks
    }
    return render(request, "bookmarks.html", context)

# def register(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your account has been successfully created!')
#             return redirect('bookmarks:login')
#     context = {'form':form}
#     return render(request, 'register.html', context)

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('bookmarks:show_main')
#         else:
#             messages.info(request, 'Sorry, incorrect username or password. Please try again.')
#     context = {}
#     return render(request, 'login.html', context)

# def logout_user(request):
#     logout(request)
#     return redirect('bookmarks:login')