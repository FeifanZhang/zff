from django.db import models
from django.utils import timezone


# Create your models here.
class WordManager(models.Manager):
    def show(self, *args, **kwargs):
        return Word.objects.filter(is_delete=False)


class Word(models.Model):
    # owner = (('wsy', "魏疏影"), ('zff', "张非凡"))
    # True: wsy; False: zff
    owner = models.BooleanField("owner", default=True)
    date_created = models.DateTimeField("date_created", auto_now_add=timezone.now)
    word = models.CharField("word", max_length=256, default="什么都没写吗？", null=False)
    is_delete = models.BooleanField("is_delete", default=False)
    objects = WordManager()


class PhotoManager(models.Manager):
    def display_list(self):
        return super().all.filter(is_delete=False)

    def create_photo(self, *args, **kwargs):
        photo = self.model()
        photo.name = kwargs["name"]
        photo.description = kwargs["description"]
        photo.save()
        return photo


class Photo(models.Model):
    name = models.CharField("name", max_length=128, unique=True, default="1")
    date_created = models.DateTimeField("date_created", default=timezone.now)
    # img = models.ImageField(upload_to='photos/')
    description = models.CharField("description", max_length=128, default="")
    is_delete = models.BooleanField("is_delete", default=False)
    objects = PhotoManager()


if __name__ == '__main__':
    Word.objects.create(owner=True, word='AAAAAA')
    Word.objects.create(owner=True, word='BBBBBB')
    Word.objects.create(owner=True, word='CCCCCCC')
