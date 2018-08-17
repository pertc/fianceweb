
from django.db import models

class Users(models.Model):

    userid=models.BigAutoField(primary_key=True)
    mobile=models.CharField(max_length=11,verbose_name='手机号',null=False)
    username=models.CharField(max_length=60,verbose_name="名称",null=False)
    passwd=models.CharField(max_length=60,verbose_name='密码',null=False)
    pay_passwd=models.CharField(max_length=60,verbose_name='支付密码',null=False)
    referee_name=models.CharField(max_length=60,verbose_name='推荐人用户名',default='admin')
    createtime=models.BigIntegerField(default=10)

    class Meta:
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        db_table = 'user'


