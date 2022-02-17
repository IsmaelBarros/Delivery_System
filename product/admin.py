from django.contrib import admin
from .models import Category, Product, Additional, Options


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'category', 'price', 'active')
    list_editable = ('price', 'active')


admin.site.register(Category)
admin.site.register(Additional)
admin.site.register(Options)
