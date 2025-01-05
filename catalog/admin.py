from django.contrib import admin

from catalog.models import Category, Product

admin.site.register(Category)
admin.site.register(Product)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ('name', 'description',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description',)

