from rest_framework import serializers
from django.core.files.base import ContentFile
import base64
from .models import *

class Base64ImageField(serializers.ImageField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    """
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            # base64 encoded image - decode
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        return super().to_internal_value(data)


class Symbols_CollectoinSerializer(serializers.ModelSerializer):
    # collection_image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    collection_image = Base64ImageField()
    class Meta:
        model = Symbols_Collectoin
        # fields = ['id', 'name', 'dimension_of_symbols', 'collection_image']
        fields = '__all__'


class symbolSerializer(serializers.ModelSerializer):
    collection_name = serializers.CharField(source='collection.name', read_only=True)
    image = Base64ImageField()

    class Meta:
        model = symbol
        fields = ['id', 'name', 'image', 'collection', 'collection_name', 'text_to_talk']

