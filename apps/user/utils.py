

from django.db.models import Q
from utils.mytime import datetime_toTimestamp
from utils.exceptions import PubErrorCustom

from apps.user.models import Users,Verification,Agent


def check_passwd(userid,passwd):
    if not Users.objects.filter(userid=userid,passwd=passwd).exists():
        return False
    return True

def check_pay_passwd(userid,passwd):
    if not Users.objects.filter(userid=userid,pay_passwd=passwd).exists():
        return False
    return True

def check_verification_code(kwargs):
    verification_code=kwargs.get('verification_code')
    mobile=kwargs.get('mobile')

    v=Verification.objects.filter(mobile=mobile,code=verification_code).order_by('-createtime')
    if v.exists():
        v=v[0]
        if v.validtime<datetime_toTimestamp():
            raise PubErrorCustom("验证码失效！")
    else:
        raise PubErrorCustom("验证码不存在！")

def check_referee_name(kwargs):
    referee_name=kwargs.get('referee_name')
    try:
        Users.objects.get(mobile=referee_name)
    except Users.DoesNotExist:
        raise PubErrorCustom("推荐人不存在！")

    agent=Agent.objects.get(Q(mobile=referee_name) | Q(mobiles__icontains=referee_name))

    agent.mobiles="{}{},".format(agent.mobiles,referee_name)
    agent.save()

def get_agent(userid):
    pass





