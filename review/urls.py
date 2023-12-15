from django.urls import path
from review.views import create_product_flutter
from review.views import show_json
from review.views import delete_ajax, show_ulasan, add_review_ajax, get_ulasan_json
from review.views import get_title_json

app_name = 'review'

urlpatterns = [
    path('', show_ulasan, name='show_ulasan'),
    path('get-ulasan/', get_ulasan_json, name='get_ulasan_json'),
    path('create-review-ajax/', add_review_ajax, name='add_review_ajax'),
    path('delete-ajax/', delete_ajax, name='delete_ajax'),
    path('json/', show_json, name='show_json'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    #path('book/<int:bookId>/', get_book_details, name='get_book_details'),
   path('get-title/', get_title_json, name='get_title_json'),
]
