from django.contrib import admin

from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name_product', 'short_description', 'description', 'price']
    search_fields = ['name_product', 'short_description', 'description']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'product', 'massage', 'datetime_created']
    search_fields = ['username', 'product', 'message']
