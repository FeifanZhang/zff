from django.contrib import admin
from homepageapp.models import *


# Register your models here.
class MyWord(admin.ModelAdmin):
    list_display = ('date_created', 'word', 'owner', 'is_delete')


class MyPhoto(admin.ModelAdmin):
    list_display = ('date_created', 'description', 'is_delete')


admin.site.register(Word, MyWord)
admin.site.register(Photo, MyPhoto)
