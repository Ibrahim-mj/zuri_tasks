from django.urls import path

from . import views

urlpatterns = [
    path('', views.info_render, name='info_render'),
]