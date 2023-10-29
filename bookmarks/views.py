import json
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from bookmarks.forms import ProductForm
from django.shortcuts import redirect, render
from django.urls import reverse
from bookmarks.models import Bookmark
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from pengelola.models import Buku


# Create your views here.
def get_bookmark_json(request):
    bookmark = Bookmark.objects.all()
    return HttpResponse(serializers.serialize('json', bookmark))

@csrf_exempt
@require_POST
def add_bookmark_ajax(request):
    data = json.loads(request.body.decode('utf-8'))
    book_id = data.get('bookId')
    # print(book_id)
    book = Buku.objects.get(pk=book_id)
    
    bookmark = Bookmark(text_number=book.text_number, title=book.title, language=book.language, first_name=book.first_name, last_name=book.last_name, year=book.year, subjects=book.subjects, bookshelves=book.bookshelves, user=request.user)
    bookmark.save()
    
    return JsonResponse({'status': 'ok'})

def show_bookmarks(request):
    bookmarks = Bookmark.objects.all()
    # user = request.user
    context = {
        'bookmarks': bookmarks
    }
    return render(request, "bookmarks.html", context)

@csrf_exempt
# @require_POST
def delete_bookmark_ajax(request):
    if request.method == "DELETE":
        try:
            data = json.loads(request.body.decode('utf-8'))
            bookmark_id = data.get('bookmarkId')
            print(bookmark_id)
            bookmark = Bookmark.objects.get(pk=bookmark_id)
            bookmark.delete()
            return JsonResponse({'status': 'ok'})
        except Bookmark.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Bookmark not found'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return HttpResponseNotFound()
    
def show_json(request):
    data = Bookmark.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# @login_required(login_url='/login')
# def show_main(request):
#     # books = Book.objects.filter(book=request.book)
#     books = Buku.objects.all()
#     # bookmarks = Bookmark.objects.all()
#     context = {
#         'books': books,
#         # 'bookmarks': bookmarks
#     }
#     return render(request, "dummymain.html", context)

# def create_product(request):
#     form = ProductForm(request.POST or None)

#     if form.is_valid() and request.method == "POST":
#         product = form.save(commit=False)
#         product.user = request.user
#         form.save()
#         return HttpResponseRedirect(reverse('bookmarks:show_main'))

#     context = {'form': form}
#     return render(request, "create_product.html", context)