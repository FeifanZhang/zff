from abc import ABC

from rest_framework import serializers


class WordSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    owner = serializers.CharField()
    date_created = serializers.DateTimeField()
    word = serializers.CharField()
