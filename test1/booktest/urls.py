from django.conf.urls import url
from booktest import views
#在应用中进行url配置的时候，需要严格匹配开头和结尾
urlpatterns=[
    # 通过url函数设置url路由的配置项
    url(r'^index$',views.index),#建立index和视图index之间的关系
    url(r'^index2$',views.index2),
    url(r'^books$',views.show_book),#显示图书信息
    url(r'^books/(\d+)$',views.detail),#这个正则表达式的数字需要用（）括起来，这样网页跳转的的时候
    #这个数字就能当做参数传递到视图函数的参数里了
]