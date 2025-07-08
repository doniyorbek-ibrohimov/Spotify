
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter

from main.views import *


router=DefaultRouter()

router.register('albums',AlbumModelViewSet)
router.register('singers',SingerModelViewSet)
router.register('songs',SongModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
