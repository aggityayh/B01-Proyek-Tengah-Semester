from django.urls import path
from bookmarks.views import show_main, create_product, add_bookmark, show_bookmarks

app_name = 'bookmarks'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('add-bookmark/<int:id>', add_bookmark, name='add_bookmark'),
    path('show-bookmarks', show_bookmarks, name='show_bookmarks'),
    # path('register/', register, name='register'),
    # path('login/', login_user, name='login'),
    # path('logout/', logout_user, name='logout'),
]