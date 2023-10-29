from django.urls import path
from review.views import delete_ajax, show_ulasan, add_review_ajax, get_ulasan_json

app_name = 'review'

urlpatterns = [
    path('', show_ulasan, name='show_ulasan'),
    path('get-ulasan/', get_ulasan_json, name='get_ulasan_json'),
    path('create-review-ajax/', add_review_ajax, name='add_review_ajax'),
    path('delete-ajax/', delete_ajax, name='delete_ajax'),
   
]
