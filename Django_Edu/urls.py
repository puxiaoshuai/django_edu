from django.contrib import admin
from django.urls import path
import xadmin
from django.views.generic import TemplateView
from  users.views import  LoginView,RegisterView
from  django.urls import include
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/', LoginView.as_view(),name='login'),
    path('register/', RegisterView.as_view(),name='register'),
    path('captcha/', include('captcha.urls')),
]
