from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password_1 = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        is_user_already_exist = User.objects.filter(username=username).exists()
        if (username == '') or (password_1 == '') or (password_2 ==''):
            return JsonResponse({
              "status": False,
              "message": "Teks tidak boleh kosong"
            }, status=401)
        elif (len(password_1)<=5):
            return JsonResponse({
              "status": False,
              "message": "Panjang password harus lebih dari 5"
            }, status=401)
        elif (password_1!=password_2):
            return JsonResponse({
              "status": False,
              "message": "Password harus sama"
            }, status=401)
        elif (not is_user_already_exist) and (password_1==password_2):
            user = User.objects.create_user(username=username,password=password_1)
            user.save()
            return JsonResponse({
                "status": True,
                "username": user.username,
            }, status=200)
        else:
            return JsonResponse({
              "status": False,
              "message": "Username sudah terdaftar"
            }, status=401)
    else:
        return JsonResponse({
            "status": "Password error"
        }, status=401)