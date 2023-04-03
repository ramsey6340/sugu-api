from rest_framework import serializers
from stores.models import *


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'num_tel1', 'num_tel2', 'email', 'categories']


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'date_created', 'date_last_updated', 'category']


class CategoryListSerializer(serializers.ModelSerializer):
    # sub_categories = SubCategoryListSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'active', 'date_created', 'date_last_updated', 'description', 'sub_categories']


class ProductListSerializer(serializers.ModelSerializer):
    # categories = CategoryListSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'date_created', 'date_last_updated', 'nb_like',
                  'min_price', 'max_price', 'is_popular', 'genre', 'store', 'sub_category', 'categories']


class SubCategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'description', 'active', 'date_created', 'date_last_updated', 'category']


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryDetailSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'active', 'date_created', 'date_last_updated', 'description', 'sub_categories']


class StoreDetailSerializer(serializers.ModelSerializer):
    categories = CategoryListSerializer(many=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'active', 'is_up_to_date', 'size', 'is_popular', 'description', 'more_precision',
                  'num_tel1', 'num_tel2', 'email', 'categories']


class ProductDetailSerializer(serializers.ModelSerializer):
    categories = CategoryDetailSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'active', 'date_created', 'date_last_updated', 'nb_like',
                  'min_price', 'max_price', 'is_popular', 'genre', 'store', 'sub_category', 'categories']
