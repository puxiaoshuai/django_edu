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

