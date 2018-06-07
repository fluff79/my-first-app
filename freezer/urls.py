from django.urls import path, re_path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    re_path(r'^post/$', views.post_list, name = 'post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path(r'^post/new/$', views.post_new, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    re_path(r'^shoppinglist/$', views.shopping_list, name='shopping_list'),
    re_path(r'^shoppinglist/(?P<pk>\d+)/$', views.shopping_list_detail, name='shopping_list_detail'),
    re_path(r'^shoppinglist/(?P<pk>\d+)/edit/$', views.shopping_list_edit, name='shopping_list_edit'),
    re_path(r'^shoppinglist/new/$', views.shopping_list_new, name='shopping_list_new'),
    re_path(r'^shoppinglist/(?P<pk>\d+)/remove/$', views.shopping_list_remove, name='shopping_list_remove')
]