from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    gender_choices = (
        ('male','男'),
        ('female','女')
    )

    nick_name = models.CharField('昵称',max_length=50,default='')
    birthday = models.DateField('生日',null=True,blank=True)
    gender = models.CharField('性别',max_length=10,choices=gender_choices,default='female')
    address = models.CharField('地址',max_length=100,default='')
    mobile = models.CharField('手机号',max_length=11,null=True,blank=True)
    # image = models.ImageField(upload_to='image/%Y%m',default='image/default.png',max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username