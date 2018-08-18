from django.db import models

# Create your models here.



class UserAction(models.Model):


    userid = models.BigIntegerField()
    activation = models.IntegerField(verbose_name="激活码",default=0)
    buypower = models.IntegerField(verbose_name="认筹权",default=0)