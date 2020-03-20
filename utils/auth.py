from loginapp import models
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        token = request._request.GET.get('token')
        token_result = models.Token.objects.confirm(token=token)
        if not token_result:
            raise exceptions.AuthenticationFailed("user confirm failed")
        else:
            return (token_result.user, token_result)

    def authenticate_header(self, request):
        pass

