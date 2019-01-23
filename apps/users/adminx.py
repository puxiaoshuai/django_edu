# coding:utf-8
__author__ = 'puxiaoshuai'
__date__ = '2019/1/23 23:26'
import xadmin
from .models import EmailVerifyRecord, Banner


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
