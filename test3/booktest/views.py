from django.shortcuts import render
from booktest.models import BookInfo
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
import requests
import base64
import json
import io
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Create your views here.
def index(request):
   return render(request,'booktest/index.html')

#
# def create(request):
#     '''新增一本图书'''
#     # 1.创建一个bookinfo对象
#     b = BookInfo()
#     b.btitle = '流星蝴蝶剑'
#     b.bpub_date = date(1990, 1, 1)
#     # 2.保存进数据库
#     b.save()
#     # 3.返回应答
#     # return HttpResponse('ok')
#     # 让浏览器返回首页
#     return HttpResponseRedirect('/index')
#
#
# def delete(request, bid):
#     '''删除点击的图书'''
#     # 1.通过bid获取图书对象
#     book = BookInfo.objects.get(id=bid)
#     # 2.删除
#     book.delete()
#     # 3.重定向到index
#     return HttpResponseRedirect('/index')
#
# def details(request,bid):
#     book=BookInfo.objects.get(id=bid)
#     heros=book.heroinfo_set.all()
#     return  render(request,'booktest/details.html',{'book':book,'heros':heros})
#
# # def index(request):
# #     return  render(request, 'booktest/index.html')
#
# def look(request):
#     API_URL = "http://127.0.0.1:5000/api/object_detect/predict"
#     IMAGE_PATH = 'image/image1.jpg'
#     fp = open(IMAGE_PATH, 'rb')
#     image_b64 = base64.b64encode(fp.read())
#     fp.close()
#     r = requests.post(API_URL, data={'image': image_b64, 'visual': True})
#     rspn = json.loads(r.text)  #需要显示到网页上的信息
#     image_b64 = rspn['image_visual']
#     image_b64decode = base64.b64decode(image_b64)
#     imageIO = io.BytesIO(image_b64decode)
#     image = Image.open(imageIO)
#     image_np = np.asarray(image)
#     plt.imsave('image/image2',image_np)
#     # plt.imshow(image_np)
#     return render(request,'booktest/look.html',{'json':rspn,'image':image_np})
#
# def image(request):
#     image_data=open('image/image1','rb').read()
#     return render(request,'booktest/look.html',{'image':image_data})