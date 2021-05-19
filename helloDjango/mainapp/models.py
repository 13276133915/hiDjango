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