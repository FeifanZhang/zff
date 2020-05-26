from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from loginapp import models
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import auth



def md5(username: str) -> str:
    import hashlib  # 局部引入md5加密算法
    import time
    ctime = str(time.time())  # 生成时间戳
    m = hashlib.md5(bytes(username, encoding='utf-8'))  # username进行md5加密
    m.update(bytes(ctime, encoding='utf-8'))  # 加入时间戳加密
    return m.hexdigest()


# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class LoginView(APIView):
    # 局部取消认证
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        try:
            username = request.data['username']
            password = request.data['password']
            user = auth.authenticate(username=username, password=password)
            if not user:
                raise ValueError("usr or pwd is wrong")
            else:
                token = md5(username=username)
                models.Token.objects.update_or_create(defaults={'token': token}, user=user)
                result = JsonResponse({"token": token})
        except ValueError as e:
            result = JsonResponse({"error": e.args}, status=404)
            print(e)
        except Exception as e:
            result = JsonResponse({"error": e.args}, status=500)
            print(e)
        return result

