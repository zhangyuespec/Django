from django.db import models


# Create your models here.

class BookInfoManger(models.Model):
    # 模型管理器类
    def all(self):  # 改变查询结果的结果集
        books = super().all()
        books = books.fliter(isDelete=False)
        return books
        # 调用父类的all方法获取所有数据，对数据进行过滤，返回books

    # 操作模型类对应的数据表（增删改查）
    def create_book(self, btitle, bpub_date):
        # book=BookInfo()这样写一缺点就是下面的BookInfo类名改变之后就会出错，应该下面这样
        model_class = self.model  # 获取self所在的模型类
        book = model_class
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        return book


# 一类
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)  # 图书名称
    bpub_date = models.DateField()  # 出版日期
    bread = models.IntegerField(default=0)  # 阅读量，默认为0
    bcomment = models.IntegerField(default=0)  # 评论量
    isDlete = models.BooleanField(default=False)  # 逻辑删除，默认不删除
    book = models.Manager()  # 自定义一个Manager对象

    # 自定义一个BookinfoManger类的对象,这是关联起模型类和模型管理器类的一句代码
    objects = BookInfoManger()

    # 封装一个类方法，可以直接用类名.调用,但是模型类一般只用来表示数据库的表，不用来写这些方法，于是把这些东西
    # 放到模型管理器类
    # @classmethod
    # def craete_book(cls,btitle,bpub_date):
    #     obj=cls()
    #     obj.btitle=btitle
    #     obj.bpub_date=bpub_date
    #     obj.save()
    #     return obj
    class Meta:
        db_table='bookinfo'


# 多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    # 定义一个关系属性
    hbook = models.ForeignKey('BookInfo')
    isDlete = models.BooleanField(default=False)  # 逻辑删除，默认不删除


class AreaInfo(models.Model):
    '''地区模型类'''
    atitle = models.CharField(max_length=20)  # 地区名称
    aparent = models.ForeignKey('self', null=True, blank=True)  # 关系属性，代表当前地区的父级，默认可以没有父级
