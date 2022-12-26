from django.contrib import admin

from .models import Beer, Order, Factory, Shop, Country
# Register your models here.

admin.site.register(Beer)
admin.site.register(Order)
admin.site.register(Factory)
admin.site.register(Shop)
admin.site.register(Country)
