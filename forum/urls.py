
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views
#from forum.views import  post_list, post_create, post_update, post_delete


urlpatterns = [

    path("list/", views.post_list, name='post_list'),
    path("create_post/", views.post_create, name='post_new'),
    path("edit_post/(?P<pk>\d+)/", views.post_update, name='post_edit'),
    path("delete/(?P<pk>\d+)/", views.post_delete, name='post_delete'),

]

