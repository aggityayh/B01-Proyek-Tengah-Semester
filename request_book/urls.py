from django.urls import path
from request_book.views import *


app_name = 'request_book'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('increase_amount/<int:product_id>/', increase_amount, name='increase_amount'),
    path('decrease_amount/<int:product_id>/', decrease_amount, name='decrease_amount'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete-product-ajax/<int:product_id>/', delete_product_ajax, name='delete_product_ajax'),
]