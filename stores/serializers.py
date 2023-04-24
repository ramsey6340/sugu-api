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


class BuyerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        exclude = ('password', 'active')


class SellerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('password', 'active')


class AddressListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class ProfileInfoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileInfo
        fields = '__all__'


class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class RegionListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = '__all__'


class NeighborhoodListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Neighborhood
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
    products = ProductListSerializer(many=True)
    category = CategoryListSerializer()
    seller = SellerListSerializer()

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
    products = ProductListSerializer(many=True)
    seller = SellerListSerializer()

    class Meta:
        model = Store
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    categories = CategoryDetailSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class BuyerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        exclude = ('password', 'active')


class SellerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('password', 'active')


class ProfileInfoDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    categories = CategoryListSerializer(many=True)
    addresses = AddressListSerializer(many=True)

    class Meta:
        model = ProfileInfo
        fields = '__all__'


class NeighborhoodDetailSerializer(serializers.ModelSerializer):
    region = RegionListSerializer()

    class Meta:
        model = Neighborhood
        fields = '__all__'


class RegionDetailSerializer(serializers.ModelSerializer):
    neighborhoods = NeighborhoodListSerializer(many=True)
    country = CountryListSerializer()

    class Meta:
        model = Region
        fields = '__all__'


class CountryDetailSerializer(serializers.ModelSerializer):
    regions = RegionListSerializer(many=True)

    class Meta:
        model = Country
        fields = '__all__'


class AddressDetailSerializer(serializers.ModelSerializer):
    country = CountryListSerializer()
    region = RegionListSerializer()
    neighborhood = NeighborhoodListSerializer()
    profile_info = ProfileInfoListSerializer()

    class Meta:
        model = Address
        fields = '__all__'


class CommentStoreDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    store = StoreListSerializer()

    class Meta:
        model = CommentStore
        fields = '__all__'


class CommentProductDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    product = ProductListSerializer()

    class Meta:
        model = CommentProduct
        fields = '__all__'


class LikeStoreDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    store = StoreListSerializer()

    class Meta:
        model = LikeStore
        fields = '__all__'


class LikeProductDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    product = ProductListSerializer()

    class Meta:
        model = LikeProduct
        fields = '__all__'


class FollowDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    store = StoreListSerializer()

    class Meta:
        model = Follow
        fields = '__all__'


class DeliveryDetailSerializer(serializers.ModelSerializer):
    address = AddressListSerializer()
    order = OrderListSerializer()
    delivery_man = DeliveryManListSerializer()

    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryManDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()

    class Meta:
        model = DeliveryMan
        fields = '__all__'


class ProductHistoryDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    products = ProductListSerializer(many=True)

    class Meta:
        model = ProductHistory
        fields = '__all__'


class CartDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    buyer = BuyerListSerializer()
    cart = CartListSerializer()
    product = ProductListSerializer()

    class Meta:
        model = Order
        fields = '__all__'


class PromotionDetailSerializer(serializers.ModelSerializer):
    seller = SellerListSerializer()
    product = ProductListSerializer()

    class Meta:
        model = Promotion
        fields = '__all__'


class TargetedAdvertisingDetailSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)
    countries = CountryListSerializer(many=True)
    regions = RegionListSerializer(many=True)
    neighborhoods = NeighborhoodListSerializer(many=True)
    seller = SellerListSerializer()
    store = StoreListSerializer()

    class Meta:
        model = TargetedAdvertising
        fields = '__all__'


# ===============> Administrateur
class BuyerDetailAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class SellerDetailAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'


class ProfileInfoDetailAdminSerializer(serializers.ModelSerializer):
    buyer = BuyerDetailAdminSerializer()
    categories = CategoryDetailSerializer(many=True)

    class Meta:
        model = ProfileInfo
        fields = '__all__'

