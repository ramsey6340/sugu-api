from django.shortcuts import render
from rest_framework import viewsets

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
            queryset = queryset.filter(categories__in=params).distinct()
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


class ProfileInfoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProfileInfoListSerializer
    detail_serializer_class = ProfileInfoDetailSerializer

    def get_queryset(self):
        return ProfileInfo.objects.filter(buyer__active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class AddressViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AddressListSerializer
    detail_serializer_class = AddressDetailSerializer

    def get_queryset(self):
        return Address.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class NeighborhoodViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NeighborhoodListSerializer
    detail_serializer_class = NeighborhoodDetailSerializer

    def get_queryset(self):
        return Neighborhood.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class RegionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RegionListSerializer
    detail_serializer_class = RegionDetailSerializer

    def get_queryset(self):
        return Region.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountryListSerializer
    detail_serializer_class = CountryDetailSerializer

    def get_queryset(self):
        return Country.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentStoreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentStoreListSerializer
    detail_serializer_class = CommentStoreDetailSerializer

    def get_queryset(self):
        return CommentStore.objects.filter(buyer__active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CommentProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentProductListSerializer
    detail_serializer_class = CommentProductDetailSerializer

    def get_queryset(self):
        return CommentProduct.objects.filter(buyer__active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class LikeStoreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LikeStoreListSerializer
    detail_serializer_class = LikeStoreDetailSerializer

    def get_queryset(self):
        return LikeStore.objects.filter(buyer__active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class LikeProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LikeProductListSerializer
    detail_serializer_class = LikeProductDetailSerializer

    def get_queryset(self):
        return LikeProduct.objects.filter(buyer__active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class DeliveryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DeliveryListSerializer
    detail_serializer_class = DeliveryDetailSerializer

    def get_queryset(self):
        return Delivery.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class FollowViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FollowListSerializer
    detail_serializer_class = FollowDetailSerializer

    def get_queryset(self):
        return Follow.objects.filter(buyer__active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class DeliveryManViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DeliveryManListSerializer
    detail_serializer_class = DeliveryManDetailSerializer

    def get_queryset(self):
        return DeliveryMan.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProductHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductHistoryListSerializer
    detail_serializer_class = ProductHistoryDetailSerializer

    def get_queryset(self):
        return ProductHistory.objects.filter(buyer__active=True)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class CartViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CartListSerializer
    detail_serializer_class = CartDetailSerializer

    def get_queryset(self):
        return Cart.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderListSerializer
    detail_serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class PromotionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PromotionListSerializer
    detail_serializer_class = PromotionDetailSerializer

    def get_queryset(self):
        return Promotion.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class TargetedAdvertisingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TargetedAdvertisingListSerializer
    detail_serializer_class = TargetedAdvertisingDetailSerializer

    def get_queryset(self):
        return TargetedAdvertising.objects.filter()

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


class AdminProfileInfoViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileInfoListSerializer
    detail_serializer_class = ProfileInfoDetailSerializer

    def get_queryset(self):
        return ProfileInfo.objects.all()

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


class AdminAddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressListSerializer
    detail_serializer_class = AddressDetailSerializer

    def get_queryset(self):
        return Address.objects.all()

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


class AdminNeighborhoodViewSet(viewsets.ModelViewSet):
    serializer_class = NeighborhoodListSerializer
    detail_serializer_class = NeighborhoodDetailSerializer

    def get_queryset(self):
        return Neighborhood.objects.all()

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


class AdminRegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionListSerializer
    detail_serializer_class = RegionDetailSerializer

    def get_queryset(self):
        return Region.objects.all()

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


class AdminCountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountryListSerializer
    detail_serializer_class = CountryDetailSerializer

    def get_queryset(self):
        return Country.objects.all()

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


class AdminCommentStoreViewSet(viewsets.ModelViewSet):
    serializer_class = CommentStoreListSerializer
    detail_serializer_class = CommentStoreDetailSerializer

    def get_queryset(self):
        return CommentStore.objects.all()

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


class AdminCommentProductViewSet(viewsets.ModelViewSet):
    serializer_class = CommentProductListSerializer
    detail_serializer_class = CommentProductDetailSerializer

    def get_queryset(self):
        return CommentProduct.objects.all()

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


class AdminLikeStoreViewSet(viewsets.ModelViewSet):
    serializer_class = LikeStoreListSerializer
    detail_serializer_class = LikeStoreDetailSerializer

    def get_queryset(self):
        return LikeStore.objects.all()

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


class AdminLikeProductViewSet(viewsets.ModelViewSet):
    serializer_class = LikeProductListSerializer
    detail_serializer_class = LikeProductDetailSerializer

    def get_queryset(self):
        return LikeProduct.objects.all()

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


class AdminDeliveryViewSet(viewsets.ModelViewSet):
    serializer_class = DeliveryListSerializer
    detail_serializer_class = DeliveryDetailSerializer

    def get_queryset(self):
        return Delivery.objects.all()

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


class AdminFollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowListSerializer
    detail_serializer_class = FollowDetailSerializer

    def get_queryset(self):
        return Follow.objects.all()

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


class AdminDeliveryManViewSet(viewsets.ModelViewSet):
    serializer_class = DeliveryManListSerializer
    detail_serializer_class = DeliveryManDetailSerializer

    def get_queryset(self):
        return DeliveryMan.objects.all()

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


class AdminProductHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductHistoryListSerializer
    detail_serializer_class = ProductHistoryDetailSerializer

    def get_queryset(self):
        return ProductHistory.objects.all()

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


class AdminCartViewSet(viewsets.ModelViewSet):
    serializer_class = CartListSerializer
    detail_serializer_class = CartDetailSerializer

    def get_queryset(self):
        return Cart.objects.all()

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


class AdminOrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderListSerializer
    detail_serializer_class = OrderDetailSerializer

    def get_queryset(self):
        return Order.objects.all()

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


class AdminPromotionViewSet(viewsets.ModelViewSet):
    serializer_class = PromotionListSerializer
    detail_serializer_class = PromotionDetailSerializer

    def get_queryset(self):
        return Promotion.objects.all()

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


class AdminTargetedAdvertisingViewSet(viewsets.ModelViewSet):
    serializer_class = TargetedAdvertisingListSerializer
    detail_serializer_class = TargetedAdvertisingDetailSerializer

    def get_queryset(self):
        return TargetedAdvertising.objects.all()

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
