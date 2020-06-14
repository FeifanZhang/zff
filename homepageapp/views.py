from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from homepageapp.models import *
from utils.serializer import *
import os
from rest_framework import exceptions
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.
class WordView(APIView):
    # add word
    def post(self, request, *args, **kwargs):
        try:
            owner = request.data.getlist('owner')[0]
            word = request.data.getlist('word')[0]
            word_save = Word.objects.insert(owner=owner, word=word)
            ret = JsonResponse({'word': word_save})
        except ValueError as e:
            ret = JsonResponse({'error': e.args}, status=409)
            print(e)
        except Exception as e:
            ret = JsonResponse({"error": e.args})
            print(e)
        return ret

    # get word
    def get(self, request, *args, **kwargs):
        try:
            wsywords = Word.objects.show(owner='wsy')
            zffwords = Word.objects.show(owner='zff')
            ret = JsonResponse({'wsywords': WordSerializers(instance=wsywords, many=True).data, 'zffwords': WordSerializers(instance=zffwords, many=True).data}, safe=False)
        except Exception as e:
            ret = JsonResponse({"error": e.args}, status=404)
            print(e)
        return ret

    # delete word
    def delete(self, request, *args, **kwargs):
        try:
            word_id = request.data.getlist('id')[0]
            word_obj = Word.objects.get(id=word_id)
            word_obj.delete()
            ret = JsonResponse({'msg': 'delete success'}, status=200)
        except Exception as e:
            ret = JsonResponse({'error': e.args}, status=404)
            print(e)
        return ret

    def put(self, request, *args, **kwargs):
        try:
            word_id = request.data.getlist('id')[0]
            word = request.data.getlist('word')[0]
            owner = request.data.getlist('owner')[0]
            word_obj = Word.objects.get(id=word_id)
            word_obj.update(word=word, owner=owner)
            ret = JsonResponse({'msg': 'update success'}, status=200)
        except Exception as e:
            ret = JsonResponse({'error': e.args}, status=404)
            print(e)
        return ret


class PhotoView(APIView):

    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        try:
            photos = Photo.objects.show()
            ret = JsonResponse({'photos': PhotoSerializers(instance=photos, many=True).data}, safe=False)
        except Exception as e:
            # 404 没有照片
            ret = JsonResponse({"error": e.args}, status=404)
            print(e)
        return ret

    def delete(self, request, *args, **kwargs):
        pass


class PhotoBackupView(APIView):

    def post(self, request, *args, **kwargs):
        path = '/Users/feifanzhang/zff/media/photos'
        result = os.listdir(path)
        photos = []
        for i in result:
            photos.append(Photo.objects.create_photo(info=i.split('.')[0], src='photos/'+i))
        ret = JsonResponse({'photos': PhotoSerializers(instance=photos, many=True).data}, safe=False)
        return ret
