from api.views import RecordViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, RecordViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('records', RecordViewSet)
router.register('ratings', RatingViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
