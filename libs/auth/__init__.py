
from utils.log import logger
from core.http.response import res_code, ResCode
from apps.user.models import Users,Token

def get_user(request):
    """
    Return the user model instance associated with the given request session.
    If no user is retrieved, return an instance of `AnonymousUser`.
    """

    token = request.META.get('HTTP_AUTHORIZATION')
    if not token:
        return (None,'token不存在', 400, ResCode.Token_Missing)

    try:
        result=Token.objects.get(key=token)
    except Token.DoesNotExist:
        return (None,'token失效！', 500, ResCode.Token_Missing)

    user=Users.objects.get(userid=result.userid)

    return (user,'操作成功！', 200, ResCode.Success)
