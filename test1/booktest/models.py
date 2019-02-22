from django.db import models
#设计和表对应的类，模型类
# Create your models here.

#一类
class BookInfo(models.Model):#相当于表
    '''图书模型类'''
    btitle = models.CharField(max_length=20)#相当于表中的字段
    bpub_data = models.DateField()#图书的出版日期，DateField说明是一个日期类型

    def __str__(self):
        return self.btitle#使Django管理现实书名

#关系属性，hbook,建立图书类和英雄人物类之间的一对多关系
#多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)#布尔类型表示性别,默认代表男
    hcomment = models.CharField(max_length=128)#备注
    #关系属性对应的表的字段名格式：关系属性名_id
    hbook = models.ForeignKey('BookInfo')#建立图书类和英雄人物类之间的一对多关系
