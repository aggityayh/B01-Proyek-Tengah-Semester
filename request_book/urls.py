from django.urls import path
from request_book.views import *

app_name = 'request_book'

urlpatterns = [
    path('', show_request_book, name='show_request_book'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('create-book-ajax/', create_request_ajax, name='add_book_ajax'),
    path('get-book/', get_book_json, name='get_book_json'),
]