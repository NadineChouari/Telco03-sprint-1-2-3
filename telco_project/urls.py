
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from .views import *



urlpatterns = [

    path('admin/', admin.site.urls),
    path("", include("authentication.urls")), 
    path('forum',include(('forum.urls', 'blog_posts'), namespace='blog_posts')),

    # The home page
    path('', views.index, name='home'),
    #other pages of sidebar
    path('pages/page-user', views.profile, name='profile'),
    path('pages/ui-forum', views.forum, name='forum'),
    path('pages/calendar', views.calendar, name='calendar'),
    path('pages/ui-tables', views.users, name='users'),
    path('pages/ui-notifications', views.notifications, name='notifications'),  
    path('pages/post_detail', views.post_detail, name='post_detail'),
    path('pages/maps', views.maps, name='maps'),
]
