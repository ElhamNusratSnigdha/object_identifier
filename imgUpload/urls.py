from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('imageupload/', views.imageupload, name='imageupload'),
    path('result/', views.result, name='result'),
]