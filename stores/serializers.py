from rest_framework import serializers
from stores.models import *


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProfileInfoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileInfo
        fields = '__all__'


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class NeighborhoodListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CommentStoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentStore
        fields = '__all__'


class CommentProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProduct
        fields = '__all__'


class LikeStoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeStore
        fields = '__all__'


class LikeProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields = '__all__'


class FollowListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class DeliveryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryManListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = '__all__'


class ProductHistoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHistory
        fields = '__all__'


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PromotionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class TargetedAdvertisingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetedAdvertising
        fields = '__all__'


class SubCategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryDetailSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


class StoreDetailSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)

    class Meta:
        model = Store
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    categories = CategoryDetailSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProfileInfoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileInfo
        fields = '__all__'


class AddressDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class NeighborhoodDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'


class RegionDetailSerializer(serializers.ModelSerializer):
    neighborhoods = NeighborhoodDetailSerializer(many=True)

    class Meta:
        model = Region
        fields = '__all__'


class CountryDetailSerializer(serializers.ModelSerializer):
    regions = RegionDetailSerializer(many=True)

    class Meta:
        model = Country
        fields = '__all__'


class CommentStoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentStore
        fields = '__all__'


class CommentProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentProduct
        fields = '__all__'


class LikeStoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeStore
        fields = '__all__'


class LikeProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeProduct
        fields = '__all__'


class FollowDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = '__all__'


class DeliveryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryManDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryMan
        fields = '__all__'


class ProductHistoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHistory
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PromotionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class TargetedAdvertisingDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetedAdvertising
        fields = '__all__'
