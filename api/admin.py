from django.contrib import admin
from .models import Product, Category, CartItem, Profile
from django.contrib.auth.models import User


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', "price", "quantity", "available", 'created',"discount")
    search_fields = ("name", "category",)
    date_hierarchy = "created"
    list_editable = ['price', 'available', 'quantity', "discount"]
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "is_lux")
    list_editable = ['is_lux']
    prepopulated_fields = {'slug': ("name",)}
admin.site.register(CartItem)
admin.site.register(Profile)
