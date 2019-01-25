from django.contrib import admin
from django.urls import path
import xadmin
from django.views.generic import TemplateView
from users.views import (LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdView
,ModifyPwdView,LogoutView)
from django.urls import include

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    path('active/<str:active_code>/', ActiveUserView.as_view()),
    path('forgetpwd/', ForgetPwdView.as_view(), name='forget_pwd'),
    path('reset_pwd/<str:active_code>/', ResetPwdView.as_view(),name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(),name='modify_pwd'),
]
