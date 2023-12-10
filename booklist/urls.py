from django.urls import path
from booklist.views import show_booklist, get_book_json, get_buku_json, add_book_ajax, delete_book_ajax, delete_book_flutter

app_name = 'booklist'

urlpatterns = [
    path('', show_booklist, name='show_booklist'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('get-buku/', get_buku_json, name='get_buku_json'),
    path('create-book-ajax/', add_book_ajax, name='add_book_ajax'),
    path('delete-book-ajax/', delete_book_ajax, name='delete_book_ajax'),
    path('delete-book-flutter/', delete_book_flutter, name='delete_book_flutter'),
]