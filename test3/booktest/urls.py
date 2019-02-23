from django.conf.urls import include, url,patterns
from django.contrib import admin
from booktest import views


urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^index$',views.index),

    # url(r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/zhangyue/图片/bji8/test2/image'}),
]