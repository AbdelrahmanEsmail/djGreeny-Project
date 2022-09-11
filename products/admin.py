from django.contrib import admin
from .models import Product, ProductImage, Category, Brand, ProductReview


class ProductImageTabular(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['id', 'name', 'flag', 'quantity', 'price']
    list_filter = ['flag', 'brand', 'category']
    search_fields = ['name', 'desc', 'subtitle']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
