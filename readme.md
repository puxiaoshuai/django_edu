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
![image.png](https://upload-images.jianshu.io/upload_images/4908477-b1fb780f8a2bcc7b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

model设计
![image.png](https://upload-images.jianshu.io/upload_images/4908477-05cfeeabd121631b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)