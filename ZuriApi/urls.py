from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^api/(?P<slack_name>\w+)/(?P<track>\w+)/$', views.info_render, name='info_render'),
]