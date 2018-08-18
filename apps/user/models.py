import binascii
import os
import random
import time
import datetime
from django.db import models
from django.utils import timezone

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

class Login(models.Model):

    mobile=models.CharField(max_length=11,verbose_name='手机号',null=False)
    createtime=models.BigIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.createtime:
            self.createtime = time.mktime(timezone.now().timetuple())
        return super(Login, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '用户登录表'
        verbose_name_plural = verbose_name
        db_table = 'login'

class Users(models.Model):

    userid=models.BigAutoField(primary_key=True)
    mobile=models.CharField(max_length=11,verbose_name='手机号',null=False)
    username=models.CharField(max_length=60,verbose_name="名称",default='')
    passwd=models.CharField(max_length=60,verbose_name='密码',null=False)
    pay_passwd=models.CharField(max_length=60,verbose_name='支付密码',null=False)
    referee_name=models.CharField(max_length=60,verbose_name='推荐人手机号')
    createtime=models.BigIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.createtime:
            self.createtime = time.mktime(timezone.now().timetuple())
        if not self.username:
            self.username = self.mobile
        return super(Users, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        db_table = 'user'

class UserDetail(models.Model):
    userid=models.BigIntegerField()
    idcard=models.CharField(max_length=20,verbose_name="身份证号",null=False)
    name=models.CharField(max_length=60,verbose_name="真实姓名",null=False)
    alipay=models.CharField(max_length=60,verbose_name="支付宝",null=False)
    wechat=models.CharField(max_length=60,verbose_name="微信",null=False)
    bank=models.CharField(max_length=60,verbose_name="银行名称",null=False)
    bank_account=models.CharField(max_length=60,verbose_name="银行账户",null=False)

    class Meta:
        verbose_name = '用户详情'
        verbose_name_plural = verbose_name
        db_table = 'userdetail'

class Verification(models.Model):
    mobile = models.CharField(max_length=11)
    code = models.CharField(max_length=4,default='')
    validtime = models.BigIntegerField(default=0)
    createtime = models.BigIntegerField(default=0)

    def save(self, *args, **kwargs):
        valid = 3  # min
        if not self.code:
            self.code = str(random.randint(1000, 9999))
        t=timezone.now()
        if not self.createtime:
            self.createtime = time.mktime(t.timetuple())
        if not self.validtime :
            self.validtime = t + datetime.timedelta(minutes=valid)
            self.validtime = time.mktime(self.validtime.timetuple())
        return super(Verification, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '验证码表'
        verbose_name_plural = verbose_name
        db_table = 'verification'

class Account(models.Model):

    userid = models.BigIntegerField()
    activation = models.IntegerField(verbose_name="激活码",default=0)
    buypower = models.DecimalField(verbose_name="认筹权",default=0.0,max_digits=18,decimal_places=2)
    integral = models.DecimalField(verbose_name='VIP分',default=0.0,max_digits=18,decimal_places=2)
    bonus =  models.DecimalField(verbose_name="股权分红",default=0.0,max_digits=18,decimal_places=2)
    spread = models.DecimalField(verbose_name="推广股权",default=0.0,max_digits=18,decimal_places=2)

    class Meta:
        verbose_name = '用户账户余额表'
        verbose_name_plural = verbose_name
        db_table = 'account'


class Agent(models.Model):
    mobile = models.CharField(max_length=11)
    mobiles = models.TextField(verbose_name="代理线",default="")

    class Meta:
        verbose_name = '代理线'
        verbose_name_plural = verbose_name
        db_table = 'agent'


