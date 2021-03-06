###### 新建项目，添加忽略文件，生成默认数据表
##### 创建users  model，继承AbstractUser,覆盖原来的
 settings.py中设置  AUTH_USER_MODEL='users.UserProfile'
 null=True,blank=True
 ```
null 是针对数据库而言，如果 null=True, 表示数据库的该字段可以为空。
blank 是针对表单的，如果 blank=True，表示你的表单填写该字段的时候可以不填
```
##### 避免循环引用
分层设计
![image.png](https://upload-images.jianshu.io/upload_images/4908477-b1fb780f8a2bcc7b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/400)

model设计
![image.png](https://upload-images.jianshu.io/upload_images/4908477-05cfeeabd121631b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/400)
![image.png](https://upload-images.jianshu.io/upload_images/4908477-615e2876300659dc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/400)
![image.png](https://upload-images.jianshu.io/upload_images/4908477-cb14ea14d217807e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/400)
##### 添加 apps，
选中apps,移动到apps下时候，去掉search xx的选项
并在settings，下添加sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
这样命令行运行不会报错，部署的时候
##### xadmin
下载 xadmin 2,0   pip install 解压
##### 模板文件
setting-template-file-code  
```
#coding:utf-8
__author__='puxiaoshuai'
__date__='$DATE $TIME'

```
新建adminx.py
一些条件
```
list_display=['code','email','send_type','send_time']
    search_fields=['code','email','send_type']
    list_filter=['code','email','send_type','send_time']
```
##### admin全局配置
#####登录注册
path('', TemplateView.as_view(template_name='index.html'),name='index'),
基于函数
直接加载html文件,无逻辑交互
跳转方式：/login/   或者 {% url 'xx'%}
验证 authenticate
登录  使用login (request,user)
#### 自定义auth方法
在setting中设置 
AUTHENTICATION_BACKENDS= ('users.views.CustomBackend',)
值为 apps中定义的CustomBackend()
```
from django.contrib.auth.backends import ModelBackend
class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except:
            return None
```
基于类视图的登陆,
继承 from django.views.generic.base import  View，
重写 get ,post方式
#####验证码  django-simple-captcha
##### 自带加密
make_password  auth 下
#####邮箱激活
通过邮箱，密码进行保存，但是没有激活， 并且，验证码类，随机生成code,关联了这个邮箱
发送cod出去，用户点击连接，访问url,根据这个code,去查找关联的邮箱，这个邮箱在查找到user,并设置激活。
##### 找回密码
在 找回密码界面，验证码发送到填写的邮箱，邮箱中设置连接地址，点击链接地址，验证code 通过，并查询此邮箱，
验证通过，跳转到填写新密码的界面，并把email隐藏设置，根据这个隐藏的邮箱查询用户，并修改密码
##### media设置
第一步
settings.py 设置
 ```angular2html
MEDIA_URL='/media/' #读取
MEDIA_ROOT=os.path.join(BASE_DIR,'media')#存放
```
第二步：
options添加   'django.template.context_processors.media'
第三步：
url.py中添加
```angular2html
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[xx
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
第四bu使用
{{MEDIA_URL}}{{xxx}}
#### 分页库
pure_pagination
####城市过滤筛选
 html中，stringformat:'i'把字符串转int类型
 
 城市，分类关联查询，  在a中?city={{ city.id }}&ct={{ category }}
 html中循环的值，，forloop.counter 
 ####我要提问
 modelform的使用
 验证通过之后，可以直接save,commit=True就是保存到数据库
 userask_form.save(commit=True)
 #### 引申到 ajax使用
 返回json,数据
 
 urls 分发处理
 1.在 自己urls.py中定义 app_name
 2.在总的url.py中，（include(),namespace='xx'）




