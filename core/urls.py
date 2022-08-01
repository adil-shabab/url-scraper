from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('images/<str:pk>', views.singleImages, name='single-images'),
    path('url/<str:pk>', views.singleUrl, name='single-url'),
    path('history', views.history, name='history'),
    path('addtofav/<str:pk>', views.addtofav, name='add-to-fav'),
    path('removefav/<str:pk>', views.removefav, name='remove-fav'),
    # path('favourites', views.history, name='favourites'),
]
