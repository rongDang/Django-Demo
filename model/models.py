from django.db import models

# Create your models here.


class Shop(models.Model):
    # 设置id为主键，自增
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    price = models.IntegerField()

    # 解决显示不明确的项目标题
    def __str__(self):
        return self.name
