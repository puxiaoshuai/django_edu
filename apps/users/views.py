# encoding=utf-8
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile, EmailVerifyRecord
from .forms import LoginForm, RegsterForm, ForgetPsdForm, ResetPwdForm
from django.db.models import Q
from  django.urls import reverse
from django.views.generic.base import View
# Create your views here.
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import send_register_email


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


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
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', )
                else:
                    return render(request, 'index.html', {'message': "用户未激活"})
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
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'message': "该邮箱已经注册", 'register_form': register_form})
            else:
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.email = user_name
                user_profile.password = make_password(pass_word)
                user_profile.save()
                print("注册成功")
                send_register_email(email=user_name, send_type='register')
                return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form, 'message': "验证不通过"})

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


class ActiveUserView(View):
    def get(self, request, active_code):
        print(active_code)
        all_records = EmailVerifyRecord.objects.filter(code=active_code).first()
        if all_records:
            # 根据code查找到了email
            email = all_records.email
            user = UserProfile.objects.get(email=email)
            user.is_active = True
            user.save()
        else:
            return render(request, '404.html', {'message': "连接失效啦"})

        return render(request, 'login.html')


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetPsdForm()
        return render(request, 'forgetpwd.html', {'forget_pwd': forget_form})

    def post(self, request):
        forget_form = ForgetPsdForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email=email, send_type='forget')
            return render(request, 'send_sucess.html', {'message': "邮件发送成功啦"})
        else:
            return render(request, 'forgetpwd.html', {'forget_pwd': forget_form})


class ResetPwdView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code).first()
        if all_records:
            # 根据code查找到了email
            email = all_records.email
            return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, '404.html', {'message': "连接失效啦"})


class ModifyPwdView(View):
    def post(self, request):
        reset_pwdForm = ResetPwdForm(request.POST)
        if reset_pwdForm.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'message': "密码不一致"})
            user = UserProfile.objects.get(email=email)
            if user:
                user.password = make_password(password=pwd2)
                user.save()
                return render(request, 'login.html')
            else:
                return render(request, 'password_reset.html', {'message': "地址失效"})
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email': email, 'message': "验证失败"})
