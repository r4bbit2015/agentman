from django.db import models
from django.contrib.auth.models import AbstractUser
from AgentMan import settings

# Create your models here.
class ipList(models.Model):
    ip = models.CharField(max_length=64, unique=True)  # ip地址 值必须唯一
    port = models.CharField(max_length=32)  # 端口
    acc = models.FloatField()  # 正确率
    speed = models.FloatField()  # 响应速度
    anonym = models.CharField(max_length=32)  # 匿名程度
    region = models.CharField(max_length=32)  # 地区
    isDelete = models.BooleanField(default=False)  # 是否删除
    lastTime = models.DateTimeField(auto_now=True)  # 最后修改时间
    createTime = models.DateTimeField(auto_created=True)  # 入库时间
    def __str__(self):
        return f'{self.pk} {self.ip}:{self.port}'

class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip = models.ForeignKey('ipList', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}-{self.ip}'

    @classmethod
    def createRecord(cls, user, ip, isD=False):
        record = cls(user=user, ip=ip, isDelete=isD)
        return record
