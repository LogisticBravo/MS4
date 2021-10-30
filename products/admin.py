from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'brand',
        'model_name',
        'product_name',
        'category',
        'price',
        'rating',
        'image',
        'image_url',
        'launched',
    )

    ordering = ('brand',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
