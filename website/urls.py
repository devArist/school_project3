from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
