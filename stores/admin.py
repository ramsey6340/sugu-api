from django.contrib import admin
from stores.models import *


class BuyerAdmin(admin.ModelAdmin):
    # list_display = ('id', 'first_name', 'last_name', 'email', 'num_tel', 'password',)
    list_display = [f.name for f in Buyer._meta.fields]


class SellerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Seller._meta.fields]


class StoreAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Store._meta.fields]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Category._meta.fields]


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in SubCategory._meta.fields]


class ProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Product._meta.fields]


class ProfileInfoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProfileInfo._meta.fields]


class PromotionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Promotion._meta.fields]


class TargetedAdvertisingAdmin(admin.ModelAdmin):
    list_display = [f.name for f in TargetedAdvertising._meta.fields]


class OrderAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Order._meta.fields]


class CardAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cart._meta.fields]


class ProductHistoryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ProductHistory._meta.fields]


class DeliveryManAdmin(admin.ModelAdmin):
    list_display = [f.name for f in DeliveryMan._meta.fields]


class DeliveryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Delivery._meta.fields]


class FollowAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Follow._meta.fields]


class LikeProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in LikeProduct._meta.fields]


class LikeStoreAdmin(admin.ModelAdmin):
    list_display = [f.name for f in LikeStore._meta.fields]


class CommentProductAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CommentProduct._meta.fields]


class CommentStoreAdmin(admin.ModelAdmin):
    list_display = [f.name for f in CommentStore._meta.fields]


class CountryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Country._meta.fields]


class RegionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Region._meta.fields]


class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Neighborhood._meta.fields]


class AddressAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Address._meta.fields]


admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProfileInfo, ProfileInfoAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(CommentStore, CommentStoreAdmin)
admin.site.register(CommentProduct, CommentProductAdmin)
admin.site.register(LikeStore, LikeStoreAdmin)
admin.site.register(LikeProduct, LikeProductAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryMan, DeliveryManAdmin)
admin.site.register(ProductHistory, ProductHistoryAdmin)
admin.site.register(Cart, CardAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(TargetedAdvertising, TargetedAdvertisingAdmin)
admin.site.register(Promotion, PromotionAdmin)
