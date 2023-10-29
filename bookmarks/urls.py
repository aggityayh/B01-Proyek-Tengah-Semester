from django.urls import path
from bookmarks.views import add_bookmark_ajax, show_bookmarks, get_bookmark_json, delete_bookmark_ajax, show_json

app_name = 'bookmarks'

urlpatterns = [
    path('add-bookmark/', add_bookmark_ajax, name='add_bookmark_ajax'),
    path('', show_bookmarks, name='show_bookmarks'),
    path('get-bookmark/', get_bookmark_json, name='get_bookmark_json'),
    path('delete-bookmark/<int:id>', delete_bookmark_ajax, name='delete_bookmark_ajax'),
    path('json/', show_json, name='show_json'), 
]