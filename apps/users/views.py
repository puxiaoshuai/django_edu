# encoding=utf-8
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from .models import UserProfile
from .forms import LoginForm, RegsterForm
from django.db.models import Q
from django.views.generic.base import View
# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import send_register_email

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', context={'data': "hahah"})

    def post(self, request):
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            print(username + password)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'index.html', )
            else:
                return render(request, 'login.html', {'message': "账号或密码错误"})
        else:
            return render(request, 'login.html', {'form': loginform})


class RegisterView(View):
    def post(self, request):
        register_form = RegsterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(pass_word)
            user_profile.save()
            print("注册成功")
            send_register_email(email=user_name,send_type='register')
            return render(request, 'login.html')

    def get(self, request):
        register_form = RegsterForm(request.GET)
        return render(request, 'register.html', context={'register_form': register_form})


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None
