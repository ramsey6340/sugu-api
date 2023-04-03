from django.contrib import admin
from stores.models import *


class StoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'is_up_to_date', 'size', 'is_popular', 'more_precision', 'num_tel1',
                    'num_tel2', 'email', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'date_created', 'date_last_updated', 'description')


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'active', 'date_created', 'date_last_updated', 'category')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'active', 'date_created', 'date_last_updated', 'nb_like',
                    'min_price', 'max_price', 'is_popular', 'genre', 'store', 'sub_category')


admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
