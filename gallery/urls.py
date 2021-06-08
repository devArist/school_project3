from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.home, name='home'),
    path('videos', views.video, name="video"),
    path('photo_detail/<int:pk>', views.photo_detail, name='photo_detail')
]
