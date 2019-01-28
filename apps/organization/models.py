# encoding:utf-8
from django.db import models
from datetime import datetime


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='城市名')
    desc = models.CharField(max_length=200, verbose_name="描述")
    create_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# Create your models here.
# 课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name='机构名称')
    desc = models.TextField(verbose_name='机构描述')
    category=models.CharField(max_length=20,verbose_name='分类',choices=(('pxjg',"培训机构"),('gx','高校'),('gr','个人')),default='pxjg')
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    image = models.ImageField(upload_to='org/%Y/%m', verbose_name='封面图')
    address = models.CharField(max_length=50, verbose_name="地址")
    city = models.ForeignKey(CityDict, on_delete=models.CASCADE, verbose_name="所在城市")
    create_time = models.DateTimeField(default=datetime.now)
    students = models.IntegerField(default=0, verbose_name="学习数")
    courses = models.IntegerField(default=0, verbose_name="课程数")
    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='教师名')
    work_years = models.IntegerField(default=0, verbose_name="工作年限")
    work_commpany = models.CharField(max_length=50, verbose_name="就职公司")
    work_postion = models.CharField(max_length=50, verbose_name="公司职位")
    points = models.CharField(max_length=50, verbose_name="教学特点")
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏数")
    create_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "老师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
