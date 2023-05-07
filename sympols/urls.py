from django.urls import path, include
from django.http import Http404
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('symbols_collection', Symbols_CollectoinViewSet)
router.register('symbols', symbolViewSet)

urlpatterns = [
    path('rest/viewsets/', include(router.urls)),
    ]
