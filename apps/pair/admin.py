from django.contrib import admin
from .models import Customers
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    """顾客"""
    list_display = ['name', 'gender', 'hobby', 'life_maxim']



admin.site.register(Customers, CustomerAdmin)


admin.site.site_header = '管理后台'
admin.site.site_title = '测试后台'
