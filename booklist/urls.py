from django.urls import path
from booklist.views import show_booklist, get_book_json, add_book_ajax

app_name = 'booklist'

urlpatterns = [
    path('', show_booklist, name='show_booklist'),
    path('get-book/', get_book_json, name='get_book_json'),
    path('create-book-ajax/', add_book_ajax, name='add_book_ajax'),
]