# coding:utf-8
from xadmin import views

__author__ = 'puxiaoshuai'
__date__ = '2019/1/23 23:26'
import xadmin
from .models import EmailVerifyRecord, Banner


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title="后台管理"
    site_footer="@蒲小帅"
    menu_style='accordion'
class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'create_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'create_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'create_time']


xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSettings)
