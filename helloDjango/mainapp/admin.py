from django.contrib import admin
from mainapp.models import UserEntity, CateTypeEntity, FuritRntity, StoreEntity

# Register your models here.


class Useradmin(admin.ModelAdmin):
    # admin模型中显示的字段
    list_display = ('id', 'name', 'phone')
    list_per_page = 5 # 配置页数
    list_filter = ('id', 'phone') #配置分类
    search_fields = ('id', 'name') # 搜索字段


class CateTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_num')

class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'source', 'price', 'category')

class StoreAdmin(admin.ModelAdmin):
    list_display = ('id_', 'name', 'adress', 'city', 'store_type')
    # 指定表单修改的字段
    fields = ('name', 'city', 'adress', 'store_type')


# 将模型增加到站点中
admin.site.register(UserEntity, Useradmin)
admin.site.register(CateTypeEntity, CateTypeAdmin)
admin.site.register(FuritRntity, FruitAdmin)
admin.site.register(StoreEntity, StoreAdmin)