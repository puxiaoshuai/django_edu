# coding:utf-8
__author__ = 'puxiaoshuai'
__date__ = '2019/1/23 23:55'
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'create_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'create_time']


class CourseOrgAmdin(object):
    list_display = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'create_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'create_time']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_commpany', 'work_postion', 'points', 'click_num', 'fav_nums',
                    'create_time']
    search_fields = ['name', 'org', 'work_years', 'work_commpany', 'work_postion', 'points', 'click_num', 'fav_nums']
    list_filter = ['name', 'org', 'work_years', 'work_commpany', 'work_postion', 'points', 'click_num', 'fav_nums',
                   'create_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAmdin)
xadmin.site.register(Teacher, TeacherAdmin)
