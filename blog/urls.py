from django.urls import re_path
from . import views

urlpatterns =[
    path('',views.postlist, name='post_list')
    ]