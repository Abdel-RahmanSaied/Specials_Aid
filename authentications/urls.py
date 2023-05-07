from .views import *
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    ]

urlpatterns += router.urls