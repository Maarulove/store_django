from django.contrib import admin
from .models import Client, Goods, Orders
# Register your models here.

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['client', 'total_amount', "date"]
    list_per_page = 15


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount', 'date_add']
    fieldsets = [
         ('personal info',{
            'fields': ['name'],
            'description': 'Information  about Author',
            'classes': ['wide']

        }),(
        'More', {
            'fields': ['photo', 'description'],
            'classes': ['collapse']
        }
    )]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'adress']
    list_per_page = 10
    list_editable =  ['adress']
    search_fields = ['name', 'phone']