from django.db import models

# Create your models here.
class UserEntity(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=11)

    class Meta:
        # 设置表明
        db_table = 't_user'