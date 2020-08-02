from django.contrib import admin
from .models import Order, OrderItem


# se registra las tablas en el panel del administardor
class OrderItemInline(admin.TabularInline):
	model=OrderItem
	raw_id_fields=['producto']

class OrderAdmin(admin.ModelAdmin):
	list_display=['id','first_name','last_name','email','address','postal_code','city','paid','created','updated']
	list_filter=['paid','created','updated']
	inlines=[OrderItemInline]

admin.site.register(Order,OrderAdmin)
# Register your models here.
