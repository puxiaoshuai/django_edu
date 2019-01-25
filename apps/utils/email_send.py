# codeding:utf8

from users.models import EmailVerifyRecord
from random import Random

from django.core.mail import send_mail
from Django_Edu.settings import EMAIL_FROM, EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER, EMAIL_PORT


def send_register_email(email, send_type='register'):
    email_recode = EmailVerifyRecord()
    code = gennerate_random_str()
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()
    if send_type == 'register':
        email_title = "在线教育网注册激活链接"
        email_body = "请点击下面的连接进行激活：http://127.0.0.1:8000/active/{}/".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print("发送成功")
        else:
            print("发送失败")
    elif send_type == 'forget':
        email_title = "在线教育网密码重置链接"
        email_body = "请点击下面的连接进行激活：http://127.0.0.1:8000/reset_pwd/{}/".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            print("发送成功")
        else:
            print("发送失败")


def gennerate_random_str(randommax=8):
    str = ''
    chars = 'qwertyuiopasdfghjklzxcvbnZXCVBNMKJHGDDAQWERTYUIOP1234567980'
    length = len(chars) - 1
    random = Random()
    for i in range(randommax):
        # 在chars长度中随机取出，一位数，并制定chars的位置，code 就是randommax的长度8位
        str += chars[random.randint(0, length)]
    return str
