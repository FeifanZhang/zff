from django.db import models
from django.utils import timezone


# Create your models here.
class WordManager(models.Manager):
    def show(self, *args, **kwargs):
        return Word.objects.filter(is_delete=False)

    def insert(self, *args, **kwargs):
        if not Word.objects.filter(word=kwargs['word']):
            word_save = Word.objects.create(owner=kwargs['owner'], word=kwargs['word'])
            return word_save
        else:
            raise ValueError({'error': 'this word has been exist'})



class Word(models.Model):
    # owner = (('wsy', "魏疏影"), ('zff', "张非凡"))
    # True: wsy; False: zff
    owner = models.BooleanField("owner", default=True)
    date_created = models.DateTimeField("date_created", auto_now_add=timezone.now)
    word = models.CharField("word", max_length=256, default="什么都没写吗？", null=False)
    is_delete = models.BooleanField("is_delete", default=False)
    objects = WordManager()


class PhotoManager(models.Manager):
    def show(self):
        return Photo.objects.filter(is_delete=False)

    def create_photo(self, *args, **kwargs):
        photo = Photo.objects.create(info=kwargs['info'], src=kwargs['src'])
        return photo


class Photo(models.Model):
    info = models.CharField("info", max_length=128, unique=True, default="1")
    date_created = models.DateTimeField("date_created", default=timezone.now)
    src = models.ImageField(upload_to='photos', null=True)
    is_delete = models.BooleanField("is_delete", default=False)
    objects = PhotoManager()



