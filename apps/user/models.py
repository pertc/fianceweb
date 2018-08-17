import binascii
import os
import time
from django.db import models
from django.utils import timezone

class Users(models.Model):

    userid=models.BigAutoField(primary_key=True)
    mobile=models.CharField(max_length=11,verbose_name='手机号',null=False)
    username=models.CharField(max_length=60,verbose_name="名称",null=False)
    passwd=models.CharField(max_length=60,verbose_name='密码',null=False)
    pay_passwd=models.CharField(max_length=60,verbose_name='支付密码',null=False)
    referee_name=models.CharField(max_length=60,verbose_name='推荐人用户名',default='admin')
    createtime=models.BigIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.createtime:
            self.createtime = time.mktime(timezone.now().timetuple())
        return super(Users, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        db_table = 'user'


class Token(models.Model):

    key = models.CharField(max_length=160, primary_key=True)
    userid  = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = verbose_name
        db_table="user_token"

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super(Token, self).save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(80)).decode()

    def __str__(self):
        return self.key


