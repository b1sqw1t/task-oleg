from django.urls import path,include,re_path
from cat import views

urlpatterns = [

    path('',                                views.index,    name='index'),
    path('create/',                         views.create_cat, name='create_cat'),
    re_path('^cat/(?P<cat_id>\d+)?/$',      views.cat_view, name='cat_view'),
    re_path('^cat/(?P<cat_id>\d+)?/edit/$', views.cat_change, name='cat_edit'),
]
