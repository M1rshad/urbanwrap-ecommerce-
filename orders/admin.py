from django.contrib import admin
from .models import Payment, Order, OrderProduct, Coupon
# Register your models here.

admin.site.register(Payment)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Coupon)