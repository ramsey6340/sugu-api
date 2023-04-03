from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from stores.serializers import *
from stores.models import *


class StoreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = StoreListSerializer
    detail_serializer_class = StoreDetailSerializer

    def get_queryset(self):
        params = list()
        queryset = Store.objects.filter(active=True)
        categories = self.request.GET.get('categories')
        if categories is not None:
            categories = categories.replace('[', '').replace(']', '')
            for param in categories.split(','):
                params.append(param)
            queryset = queryset.filter(categories__in=params)
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class

        else:
            return super().get_serializer_class()


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serialize_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serialize_class
        else:
            return super().get_serializer_class()


class SubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SubCategoryListSerializer
    detail_serializer_class = SubCategoryDetailSerializer

    def get_queryset(self):
        return SubCategory.objects.filter(active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        params = list()
        queryset = Product.objects.filter(active=True)
        categories = self.request.GET.get('categories')
        if categories is not None:
            categories = categories.replace('[', '').replace(']', '')
            for param in categories.split(','):
                params.append(int(param))
            queryset = queryset.filter(categories__in=params).distinct()
        return queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductOfStoreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        # la clé "store_pk" est defini par le paramètre lookup de la classe NestedSimpleRouter,
        # tu donne un nom et DRF ajoute le "_pk"
        return Product.objects.filter(store=self.kwargs['store_pk'], active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductOfCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        # la clé "category_pk" est defini par le paramètre lookup de la classe NestedSimpleRouter,
        # tu donne un nom et DRF ajoute le "_pk"

        return Product.objects.filter(categories=self.kwargs['category_pk'], active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductOfSubCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        # la clé "store_pk" est defini par le paramètre lookup de la classe NestedSimpleRouter,
        # tu donne un nom et DRF ajoute le "_pk"
        return Product.objects.filter(sub_category=self.kwargs['subcategory_pk'], active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


# =======> Les serializers d'administrateur

class AdminStoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreListSerializer
    detail_serializer_class = StoreDetailSerializer

    def get_queryset(self):
        return Store.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return self.detail_serializer_class
        elif self.action == 'retrieve':
            return self.detail_serializer_class
        elif self.action == 'update':
            return self.detail_serializer_class
        elif self.action == 'partial_update':
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()


class AdminCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return self.detail_serializer_class
        elif self.action == 'retrieve':
            return self.detail_serializer_class
        elif self.action == 'update':
            return self.detail_serializer_class
        elif self.action == 'partial_update':
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()


class AdminSubCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SubCategoryListSerializer
    detail_serializer_class = SubCategoryDetailSerializer

    def get_queryset(self):
        return SubCategory.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return self.detail_serializer_class
        elif self.action == 'retrieve':
            return self.detail_serializer_class
        elif self.action == 'update':
            return self.detail_serializer_class
        elif self.action == 'partial_update':
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()


class AdminProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        return Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return self.detail_serializer_class
        elif self.action == 'retrieve':
            return self.detail_serializer_class
        elif self.action == 'update':
            return self.detail_serializer_class
        elif self.action == 'partial_update':
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()


class AdminProductOfStoreViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        # la clé "store_pk" est defini par le paramètre lookup de la classe NestedSimpleRouter,
        # tu donne un nom et DRF ajoute le "_pk"
        return Product.objects.filter(store=self.kwargs['store_pk'])

    def get_serializer_class(self):
        if self.action == 'create':
            return self.detail_serializer_class
        elif self.action == 'retrieve':
            return self.detail_serializer_class
        elif self.action == 'update':
            return self.detail_serializer_class
        elif self.action == 'partial_update':
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()


class AdminProductOfSubCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        # la clé "subcategory_pk" est defini par le paramètre lookup de la classe NestedSimpleRouter,
        # tu donne un nom et DRF ajoute le "_pk"
        return Product.objects.filter(sub_category=self.kwargs['subcategory_pk'])

    def get_serializer_class(self):
        if self.action == 'create':
            return self.detail_serializer_class
        elif self.action == 'retrieve':
            return self.detail_serializer_class
        elif self.action == 'update':
            return self.detail_serializer_class
        elif self.action == 'partial_update':
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()


class AdminProductOfCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        # la clé "category_pk" est defini par le paramètre lookup de la classe NestedSimpleRouter,
        # tu donne un nom et DRF ajoute le "_pk"

        return Product.objects.filter(categories=self.kwargs['category_pk'])

    def get_serializer_class(self):
        if self.action == 'create':
            return self.detail_serializer_class
        elif self.action == 'retrieve':
            return self.detail_serializer_class
        elif self.action == 'update':
            return self.detail_serializer_class
        elif self.action == 'partial_update':
            return self.detail_serializer_class
        else:
            return super().get_serializer_class()
