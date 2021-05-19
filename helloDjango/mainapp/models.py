import uuid

from django.db import models

# Create your models here.
class UserEntity(models.Model):
    name = models.CharField(max_length=20, verbose_name="账号")
    age = models.IntegerField(default=0, verbose_name="年龄")
    phone = models.CharField(max_length=11, verbose_name="手机号", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        # 设置表明
        db_table = 'app_user'
        verbose_name = '客户管理'
        verbose_name_plural = verbose_name


# 水果分类模型
class CateTypeEntity(models.Model):
    name = models.CharField(max_length=20,
                            verbose_name="分类名")
    order_num = models.IntegerField(verbose_name="排序字段")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_category'
        verbose_name = "水果分类表"
        verbose_name_plural = verbose_name
        ordering = ['-order_num'] # 指定排序字段 -表示降序


class FuritRntity(models.Model):
    name = models.CharField(max_length=20, verbose_name="水果名")
    price = models.FloatField(verbose_name="价格")
    source = models.CharField(max_length=50,verbose_name="原产地")
    category = models.ForeignKey(CateTypeEntity,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-"+self.source



    class Meta:
        db_table = 'app_fruit'
        verbose_name = '水果表'
        verbose_name_plural = verbose_name


class StoreEntity(models.Model):
    # 可以显示的方式声明主键
    id = models.UUIDField(primary_key=True,
                          verbose_name="商店编号")

    name = models.CharField(max_length=50,
                            verbose_name="店名",
                            unique=True) # unique唯一约束
    # 表中对应的字段 type_
    store_type = models.IntegerField(choices=((0,"自营"),(1,"第三方")),
                                     verbose_name="店铺类型",
                                     db_column="type_")

    adress = models.CharField(max_length=100,
                              verbose_name="地址")
    # 城市可能在搜索框中使用
    city = models.CharField(max_length=50,
                            verbose_name="城市",
                            db_index=True) # db_index 索引
    create_time = models.DateTimeField(verbose_name="创建时间",
                                   auto_now_add=True,
                                       null=True) # 创建当前时间
    last_time = models.DateField(verbose_name="最后变更时间",
                                 auto_now=True,
                                 null=True) # 每次更新都会增加当前时间

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # 调用模型保存方法的时候 被调用
        # 判断是否为新增的
        if not self.id:
            self.id = uuid.uuid4().hex
        super().save()


    @property
    def id_(self):
        return str(self.id).replace('-','')

    class Meta:
        db_table = "app_store"
        verbose_name = "水果店铺"
        verbose_name_plural = verbose_name
        unique_together = (('name','city'),) #组合来辨识重复值
