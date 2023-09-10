from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^api\?$', views.info_render, name='info'),
]