from django.contrib import admin
from .models import Product, ProductImage, Category, Brand, ProductReview


class ProductImageTabular(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name', 'quantity', 'price']
    list_filter = ['brand', 'category']
    search_fields = ['name', 'desc', 'subtitle']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(Brand)
admin.site.register(Category)
