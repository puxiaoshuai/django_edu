# encoding:utf-8
from django.db import models
from datetime import datetime


# Create your models here.
# 课程基本信息
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(verbose_name="课程难度", choices=(('cj', "初级"), ('zj', "中级"), ('gj', "高级")), max_length=20)
    learn_time = models.IntegerField(default=0, verbose_name="学习时长")
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    image = models.ImageField(upload_to='course/%Y/%m', verbose_name="封面图")
    click_nums = models.IntegerField(default=0, verbose_name="课程点击量")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name


####章节,跟课程是 1对多
class Chapter(models.Model):
    course = models.ForeignKey(Course, verbose_name="章节",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="章节名称")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name


class Vedio(models.Model):
    chapter = models.ForeignKey(Chapter, verbose_name="章节",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名称")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseSource(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程",on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="资源名称")
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name="下载链接", max_length=100)
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程下载资源"
        verbose_name_plural = verbose_name
