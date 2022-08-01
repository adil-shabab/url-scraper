from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('images/<str:pk>', views.singleImages, name='single-images'),
]
