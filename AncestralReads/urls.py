from django.urls import path
from AncestralReads.views import show_main

app_name = 'AncestralReads'

urlpatterns = [
    path('', show_main, name='show_main'),
]