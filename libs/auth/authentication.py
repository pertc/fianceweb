"""
Provides various authentication policies.
"""
from __future__ import unicode_literals

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from auth import get_user

class Authentication(BaseAuthentication):
    def authenticate(self, request):
        request.user, msg, status_code, rescode = get_user(request)
        detail = {
            'rescode': rescode,
            'msg': msg,
            'status_code': status_code
        }
        if status_code != '200':
            raise exceptions.APIException(detail)
        return (request.user, None)
