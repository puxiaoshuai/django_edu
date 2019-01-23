# coding:utf-8
__author__ = 'puxiaoshuai'
__date__ = '2019/1/23 23:42'
import xadmin
from .models import Course, Chapter, Vedio, CourseSource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums',
                    'create_time']
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_time', 'students', 'fav_nums', 'image', 'click_nums',
                   'create_time']


class ChapterAdmin(object):
    list_display = ['name', 'course', 'create_time']
    search_fields = ['name', 'course']
    list_filter = ['name', 'course', 'create_time']


class VedioAdmin(object):
    list_display = ['name', 'chapter', 'create_time']
    search_fields = ['name', 'chapter']
    list_filter = ['name', 'chapter', 'create_time']


class CourseSouseAdmin(object):

    list_display = ['name', 'course', 'download','create_time']
    search_fields = ['name', 'course', 'download']
    list_filter = ['name', 'course', 'download','create_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Vedio, VedioAdmin)
xadmin.site.register(CourseSource, CourseSouseAdmin)
