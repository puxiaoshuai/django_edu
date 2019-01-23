# encoding:utf-8
from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import Course


# Create your models here.
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    course_name = models.CharField(max_length=50, verbose_name="课程名称")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name


class CourseComment(models.Model):
    # 课程评论
    user = models.ForeignKey(UserProfile, verbose_name="用户",on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name="课程",on_delete=models.DO_NOTHING)
    comments = models.CharField(max_length=200, verbose_name="评论内容")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    # 用户收藏
    user = models.ForeignKey(UserProfile, verbose_name="用户",on_delete=models.DO_NOTHING)
    fav_id = models.IntegerField(default=0, verbose_name="数据ID")
    fav_type = models.IntegerField(choices=(('1', '课程'), ('2', "课程机构"), ('3', "讲师")), default=1, verbose_name="收藏类型")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    # 消息发给所有，还是固定用户
    user = models.IntegerField(default=0, verbose_name="接收用户")
    message = models.CharField(max_length=500, verbose_name="消息时间")
    has_read = models.BooleanField(default=False, verbose_name="是否已读")
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    # 记录用户学习的课程
    user = models.ForeignKey(UserProfile, verbose_name="用户",on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, verbose_name="课程",on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "用户学习课程"
        verbose_name_plural = verbose_name
