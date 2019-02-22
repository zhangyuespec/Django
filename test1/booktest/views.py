from django.shortcuts import render
from django.http import HttpResponse  #导入模块
from booktest.models import BookInfo #导入图书模型类
# Create your views here.
from django.template import loader,RequestContext

# 1.定义视图函数
#http://127.0.0.1:8000/index
def index(request):#视图函数必须有一个参数
    #进行处理，和M和T进行交互。。。
    # return  HttpResponse('good')

    # #使用模板文件
    # #1.加载模板文件,先import loader
    # temp=loader.get_template('booktest/index.html')
    # #2.定义模板上下文，向模板文件传递数据
    # context=RequestContext(request,{})
    # #3.模板渲染，得到一个标准的 html内容
    # res_html=temp.render(context)
    # #4.返回给浏览器
    # return HttpResponse(res_html)
    #简单的封装好的函数如下
    return render(request,'booktest/index.html',{'context':'peipei','list':list(range(1,10))})

# 2.进行url配置，建立url地址和视图的对应关系
def index2(requst):
    return HttpResponse('hello python')

def show_book(requset):
    '''显示图书的信息'''
    #1.通过M查找图书表中的数据
    books = BookInfo.objects.all()
    #使用模板
    return render(requset,'booktest/show_book.html',{'books':books})

def detail(request,bid):
    '''查询图书关联的信息'''
    #1.更具bid查询图书信息
    book=BookInfo.objects.get(id=bid)
    #查询和book关联的英雄信息
    heros=book.heroinfo_set.all()
    #使用模板
    return render(request,'booktest/detail.html',{'book':book,'heros':heros})