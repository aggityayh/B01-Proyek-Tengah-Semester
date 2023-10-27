from django.urls import path
from pengelola.views import register , get_books, hapus_buku, tambah_buku
from pengelola.views import login_user,edit_buku, display_books, logout_user, show_main


app_name = 'pengelola'

urlpatterns = [
    path("", show_main, name='show_main'),
    path("register/", register, name='register'),
    path("json/", get_books, name="get_books"),
    path("hapus/<int:id>", hapus_buku, name='hapus_buku'),
    path("tambah/", tambah_buku, name='tambah_buku'),
    path("display-books/", display_books, name="display_books"),
    path("login/", login_user, name='login'),
    path("edit/<int:id>", edit_buku, name="edit_buku"),
    path("logout/", logout_user, name="logout"),
]