from django.contrib import admin
from .models import Client, Order, Bottle, BottleCount

# clients/admin.py

admin.site.register(Client)
admin.site.register(Bottle)
admin.site.register(BottleCount)


class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ['name', 'contacts', 'created_at', 'finished']
    list_editable = ['finished']
    fields = ['name', 'contacts', 'created_at', 'updated_at', 'description', 'finished', 'bottles']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Order, OrderAdmin)
