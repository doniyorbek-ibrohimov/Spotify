
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('singers/',SingersAPIView.as_view()),
    path('singers/<int:pk>/',SingerRetrieveAPIView.as_view()),
]
