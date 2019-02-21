from django.db import models

# Create your models here.
#一类
class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)#图书名称
    bpub_date=models.DateField()#出版日期
    bread=models.IntegerField(default=0)#阅读量，默认为0
    bcomment=models.IntegerField(default=0)#评论量
    isDlete=models.BooleanField(default=False)#逻辑删除，默认不删除

#多类
class HeroInfo(models.Model):
    hname=models.CharField(max_length=20)
    hgender=models.BooleanField(default=False)
    hcomment=models.CharField(max_length=200)
    #定义一个关系属性
    hbook=models.ForeignKey('BookInfo')
    isDlete = models.BooleanField(default=False)  # 逻辑删除，默认不删除