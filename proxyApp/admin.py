from django.contrib import admin
from .models import ipList,Record
# Register your models here.
@admin.register(ipList)
class ipList(admin.ModelAdmin):
    list_display=['pk','ip','port','acc','speed','lastTime']
    list_filter = ['acc']
    search_fields = ['port']
    list_per_page = 20
    ordering = ['pk']
@admin.register(Record)
class Record(admin.ModelAdmin):
    list_display = ['user','ip']
    list_filter = ['user']
