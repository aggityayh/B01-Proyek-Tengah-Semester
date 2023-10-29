from django.urls import path
from bookmarks.views import add_bookmark_ajax, show_bookmarks, get_bookmark_json, delete_bookmark_ajax, show_json

app_name = 'bookmarks'

urlpatterns = [
    # path('', show_main, name='show_main'),
    # path('create-product/', create_product, name='create_product'),
    path('add-bookmark/', add_bookmark_ajax, name='add_bookmark_ajax'),
    path('show-bookmarks/', show_bookmarks, name='show_bookmarks'),
    path('get-bookmark/', get_bookmark_json, name='get_bookmark_json'),
    # path('delete-bookmark/', delete_bookmark, name='delete_bookmark'),
    path('delete-bookmark/', delete_bookmark_ajax, name='delete_bookmark_ajax'),
    path('json/', show_json, name='show_json'), 
    # path('register/', register, name='register'),
    # path('login/', login_user, name='login'),
    # path('logout/', logout_user, name='logout'),
]