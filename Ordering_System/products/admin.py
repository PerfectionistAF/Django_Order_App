from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers
import csv

# Register your models here.
from .models import Product, Order, OrderItem

##change objects of a specific entity as an admin action
##CRUD: here we use admin to update active status of products
@admin.action(description="Mark selected products inactive")
def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)

##inform our ModelAdmin of the action
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company', 'price', 'stock', 'is_active', 'last_updated_at']
    ordering = ["last_updated_at"]
    actions = [make_inactive, 'export_as_csv']

    def export_as_csv(self, request, queryset):
        fieldnames = ['id', 'name', 'company', 'price', 'stock', 'is_active']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="products.csv"'
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()

        for product in queryset:
            writer.writerow({
                'id': product.id,
                'name': product.name,
                'company': product.company.name,
                'price': product.price,
                'stock': product.stock,
                'is_active': product.is_active
            })
        return response
    export_as_csv.short_description = "Export selected products as CSV"


#Export orders as CSV with appropriate details
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'company', 'quantity', 'status', 'created_at']
    actions = ["export_orders_as_csv"]

    def export_orders_as_csv(self, request, queryset):
        fieldnames = ['id', 'product', 'company', 'quantity', 'status', 'created_at']
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exported_orders.csv"'
        writer = csv.DictWriter(response, fieldnames=fieldnames)
        writer.writeheader()
        for order in queryset:  ###authenticated, authorized user
            writer.writerow({
                'id': order.id,
                'product': order.product.name,
                'company': order.company.name,
                'quantity': order.quantity,
                'status': order.status,
                'created_at': order.created_at
            })
        return response
    export_orders_as_csv.short_description = "Export selected orders as CSV"


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
#admin.site.register(OrderItem)