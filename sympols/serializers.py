from rest_framework import serializers
from .models import *


class Symbols_CollectoinSerializer(serializers.ModelSerializer):
    collection_image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    class Meta:
        model = Symbols_Collectoin
        fields = ['id', 'name', 'dimension_of_symbols', 'collection_image']


class symbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = symbol
        fields = ['id', 'name', 'image', 'collection']

