from django.conf.urls import include, url
from django.contrib import admin
from booktest import views

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index$',views.index),
    url(r'^create$',views.create),
    url(r'^delete(\d+)$',views.delete),#删除点击的图书
    url(r'^books(\d+)$',views.details)
]