from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.info_render, name='info'),
]