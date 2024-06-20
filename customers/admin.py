from django.contrib import admin
from .models import Customer,Product,OrderItem,Order,Address,Rating


# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Address)
admin.site.register(Rating)