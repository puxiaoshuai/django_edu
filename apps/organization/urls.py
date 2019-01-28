from django.contrib import admin
from django.urls import path
import xadmin
from django.views.generic import TemplateView
from users.views import (LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdView
,ModifyPwdView,LogoutView)
from  organization.views import  OrgView,AddUserAsk_View
from django.urls import include

from django.conf import settings
from django.conf.urls.static import static
app_name='organization'
urlpatterns = [
    path('org_list/', OrgView.as_view(),name='org_list'),
    path('userask_add/', AddUserAsk_View.as_view(),name='add_userask'),
]

