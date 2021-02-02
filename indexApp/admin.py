from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models
#在admin中注册模型
admin.site.register(models.User)