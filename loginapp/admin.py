from django.contrib import admin
from loginapp.models import *


# Register your models here.
class MyUsers(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'last_login', 'is_superuser')


class MyTokens(admin.ModelAdmin):
    list_display = ('user', 'token', 'last_op_time')


admin.site.register(Users, MyUsers)
admin.site.register(Token, MyTokens)
