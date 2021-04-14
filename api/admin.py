from django.contrib import admin
from .models import Product, Category, CartItem, Profile


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """ adding the product class to the admin site """

    list_display = (
        'name', "price", "quantity", "is_available", 'created', "discount")

    search_fields = ("name", "category",)
    date_hierarchy = "created"
    list_editable = ['price', 'is_available', 'quantity', "discount"]
    prepopulated_fields = {'slug': ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ adding category class to the admin site """

    list_display = ("name", "slug", "is_lux")
    list_editable = ['is_lux']
    prepopulated_fields = {'slug': ("name",)}


admin.site.register(CartItem)
admin.site.register(Profile)
