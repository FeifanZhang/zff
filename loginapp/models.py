from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
from rest_framework import exceptions


# Create your models here.
class Users(AbstractUser):
    pass


class TokenManager(models.Manager):
    def confirm(self, *args, **kwargs):
        try:
            token = Token.objects.get(token=kwargs["token"])  # token和user是一对一关系，所以用get
            if (timezone.now() - token.last_op_time).seconds >= 30*10:  # 判断距离上一次访问是否超过30分钟
                raise exceptions.AuthenticationFailed("the token expired, login again")
            else:
                token.save()  # token里的时间属性带有auto_now字段，通过save可以激活时间属性自动更新时间
        except Exception as e:
            raise exceptions.AuthenticationFailed(e.args)
        return token


class Token(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    token = models.CharField("token", unique=True, max_length=128)
    last_op_time = models.DateTimeField("last_op_time", auto_now=True)
    objects = TokenManager()


# while reset, run this script to recover user info
if __name__ == '__main__':
    Users.objects.create_superuser(username="feifanzhang", password="Zff19970329", email="zhang6025@ulwax.edu")
    Users.objects.create_user(username="19960115", password="19970329", email="zhang6025@ulwax.edu")
