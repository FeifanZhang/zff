from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from homepageapp.models import *
from utils.serializer import *
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
            Word.objects.create(owner=owner, word=word)
            ret = {'msg': 'save success'}
        except Exception as e:
            ret = {"error": e.args}
            print(e)
        if not ret:
            ret = {'msg': 'word post method neither exe try nor except'}
        return JsonResponse(ret)

    # get word
    def get(self, request, *args, **kwargs):
        try:
            words = Word.objects.show()
            ret = JsonResponse(WordSerializers(instance=words, many=True).data, safe=False)
        except Exception as e:
            ret = JsonResponse({"error": e.args}, status=404)
            print(e)
        if not ret:
            ret = JsonResponse({'error': 'no words in here'}, status=403)
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
        pass

    def delete(self, request, *args, **kwargs):
        pass
