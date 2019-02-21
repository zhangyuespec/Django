from django.shortcuts import render
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    # 1.查询出所有图书的信息
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/index.html', {'books': books})


def create(request):
    '''新增一本图书'''
    # 1.创建一个bookinfo对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990, 1, 1)
    # 2.保存进数据库
    b.save()
    # 3.返回应答
    # return HttpResponse('ok')
    # 让浏览器返回首页
    return HttpResponseRedirect('/index')


def delete(request, bid):
    '''删除点击的图书'''
    # 1.通过bid获取图书对象
    book = BookInfo.objects.get(id=bid)
    # 2.删除
    book.delete()
    # 3.重定向到index
    return HttpResponseRedirect('/index')

def details(request,bid):
    book=BookInfo.objects.get(id=bid)
    heros=book.heroinfo_set.all()
    return  render(request,'booktest/details.html',{'book':book,'heros':heros})