from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from .permissons import *
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


class Symbols_CollectoinViewSet(viewsets.ModelViewSet):
    queryset = Symbols_Collectoin.objects.all()
    serializer_class = Symbols_CollectoinSerializer
    permission_classes = [UserPermission]



class symbolViewSet(viewsets.ModelViewSet):
    queryset = symbol.objects.all()
    serializer_class = symbolSerializer
    permission_classes = [UserPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'collection__id']
    search_fields = ['name', 'text_to_talk']
    lookup_field = 'id'

