from django.contrib import admin
from django.urls import path, include
from stores.views import *
from rest_framework_nested import routers

router = routers.SimpleRouter()

# ========> Enregistrement des URLs de base

# api/stores/ and api/stores/{store_pk}/ and api/stores/?categories=[category_id1, category_id2, ...]
router.register('stores', StoreViewSet, basename='stores')

# api/categories/ and api/categories/{category_pk}/
router.register('categories', CategoryViewSet, basename='categories')

# api/subcategories/ and api/subcategories/{subcategory_pk}/
router.register('subcategories', SubCategoryViewSet, basename='sub-categories')

# api/products/ and api/products/{product_pk}/ and api/products/?categories=[category_id1, category_id2, ...]
router.register('products', ProductViewSet, basename='products')

# api/profileinfos/ and api/profileinfos/{profileinfo_pk}/
router.register('profileinfos', ProfileInfoViewSet, basename='profileinfos')

# api/addresses/ and api/addresses/{address_pk}/
router.register('addresses', AddressViewSet, basename='addresses')

# api/neighborhoods/ and api/neighborhoods/{neighborhood_pk}/
router.register('neighborhoods', NeighborhoodViewSet, basename='neighborhoods')

# api/regions/ and api/regions/{region_pk}/
router.register('regions', RegionViewSet, basename='regions')

# api/countries/ and api/countries/{country_pk}/
router.register('countries', CountryViewSet, basename='countries')

# api/commentsstores/ and api/commentsstores/{commentstore_pk}/
router.register('commentsstores', CommentStoreViewSet, basename='commentsstores')

# api/commentsproducts/ and api/commentsproducts/{commentproduct_pk}/
router.register('commentsproducts', CommentProductViewSet, basename='commentsproducts')

# api/likesstores/ and api/likesstores/{likestore_pk}/
router.register('likesstores', LikeStoreViewSet, basename='likesstores')

# api/likesproducts/ and api/likesproducts/{likeproduct_pk}/
router.register('likesproducts', LikeProductViewSet, basename='likesproducts')

# api/follows/ and api/follows/{follow_pk}/
router.register('follows', FollowViewSet, basename='follows')

# api/deliveries/ and api/deliveries/{delivery_pk}/
router.register('deliveries', DeliveryViewSet, basename='deliveries')

# api/deliverymen/ and api/deliverymen/{deliveryman_pk}/
router.register('deliverymen', DeliveryManViewSet, basename='deliverymen')

# api/productshistories/ and api/productshistories/{producthistory_pk}/
router.register('productshistories', ProductHistoryViewSet, basename='productshistories')

# api/carts/ and api/carts/{cart_pk}/
router.register('carts', CartViewSet, basename='carts')

# api/orders/ and api/orders/{order_pk}/
router.register('orders', OrderViewSet, basename='orders')

# api/targetedads/ and api/targetedads/{targetedadvertising_pk}/
router.register('targetedads', TargetedAdvertisingViewSet, basename='targetedads')

# api/promotions/ and api/promotions/{promotion_pk}/
router.register('promotions', PromotionViewSet, basename='promotions')


# api/admin/stores/ and api/admin/stores/{store_pk}/
router.register('admin/stores', AdminStoreViewSet, basename='admin-stores')

# api/admin/categories/ and api/admin/categories/{category_pk}/
router.register('admin/categories', AdminCategoryViewSet, basename='admin-categories')

# api/admin/subcategories/ and api/admin/subcategories/{subcategory_pk}/
router.register('admin/subcategories', AdminSubCategoryViewSet, basename='admin-sub-categories')

# api/admin/products/ and api/admin/products/{product_pk}/
router.register('admin/products', AdminProductViewSet, basename='admin-products')

# api/admin/profileinfos/ and api/admin/profileinfos/{profileinfo_pk}/
router.register('admin/profileinfos', AdminProfileInfoViewSet, basename='admin-profileinfos')

# api/admin/addresses/ and api/admin/addresses/{address_pk}/
router.register('admin/addresses', AdminAddressViewSet, basename='admin-addresses')

# api/admin/neighborhoods/ and api/admin/neighborhoods/{neighborhood_pk}/
router.register('admin/neighborhoods', AdminNeighborhoodViewSet, basename='admin-neighborhoods')

# api/admin/regions/ and api/admin/regions/{region_pk}/
router.register('admin/regions', AdminRegionViewSet, basename='admin-regions')

# api/admin/countries/ and api/admin/countries/{country_pk}/
router.register('admin/countries', AdminCountryViewSet, basename='admin-countries')

# api/admin/commentsstores/ and api/admin/commentsstores/{commentstore_pk}/
router.register('admin/commentsstores', AdminCommentStoreViewSet, basename='admin-commentsstores')

# api/admin/commentsproducts/ and api/admin/commentsproducts/{commentproduct_pk}/
router.register('admin/commentsproducts', AdminCommentProductViewSet, basename='admin-commentsproducts')

# api/admin/likesstores/ and api/admin/likesstores/{likestore_pk}/
router.register('admin/likesstores', AdminLikeStoreViewSet, basename='admin-likesstores')

# api/admin/likesproducts/ and api/admin/likesproducts/{likeproduct_pk}/
router.register('admin/likesproducts', AdminLikeProductViewSet, basename='admin-likesproducts')

# api/admin/follows/ and api/admin/follows/{follow_pk}/
router.register('admin/follows', AdminFollowViewSet, basename='admin-follows')

# api/admin/deliveries/ and api/admin/deliveries/{delivery_pk}/
router.register('admin/deliveries', AdminDeliveryViewSet, basename='admin-deliveries')

# api/admin/deliverymen/ and api/deliverymen/{deliveryman_pk}/
router.register('admin/deliverymen', AdminDeliveryManViewSet, basename='admin-deliverymen')

# api/admin/productshistories/ and api/admin/productshistories/{producthistory_pk}/
router.register('admin/productshistories', AdminProductHistoryViewSet, basename='admin-productshistories')

# api/admin/carts/ and api/admin/carts/{cart_pk}/
router.register('admin/carts', AdminCartViewSet, basename='admin-carts')

# api/admin/orders/ and api/admin/orders/{order_pk}/
router.register('admin/orders', AdminOrderViewSet, basename='admin-orders')

# api/admin/targetedads/ and api/admin/targetedads/{targetedadvertising_pk}/
router.register('admin/targetedads', AdminTargetedAdvertisingViewSet, basename='admin-targetedads')

# api/admin/promotions/ and api/admin/promotions/{promotion_pk}/
router.register('admin/promotions', AdminPromotionViewSet, basename='admin-promotions')


# ========> Fin d'enregistrement des URLs de base

store_router = routers.NestedSimpleRouter(router, 'stores', lookup='store')
category_router = routers.NestedSimpleRouter(router, 'categories', lookup='category')
sub_category_router = routers.NestedSimpleRouter(router, 'subcategories', lookup='subcategory')

admin_store_router = routers.NestedSimpleRouter(router, 'admin/stores', lookup='store')
admin_category_router = routers.NestedSimpleRouter(router, 'admin/categories', lookup='category')
admin_sub_category_router = routers.NestedSimpleRouter(router, 'admin/subcategories', lookup='subcategory')

# ========> Enregistrement des URLs de dépendance

# api/stores/{store_pk}/products and api/stores/{store_pk}/products/{product_pk/
store_router.register('products', ProductOfStoreViewSet, basename='products-store')

# api/categories/{category_pk}/products and api/categories/{category_pk}/products/{product_pk/
category_router.register('products', ProductOfCategoryViewSet, basename='products-category')

# api/subcategories/{subcategory_pk}/products and api/subcategories/{subcategory_pk}/products/{product_pk/
sub_category_router.register('products', ProductOfSubCategoryViewSet, basename='products-sub-category')

# api/admin/stores/{store_pk}/products and api/admin/stores/{store_pk}/products/{product_pk/
admin_store_router.register('products', AdminProductOfStoreViewSet, basename='admin-products-store')

# api/admin/categories/{category_pk}/products and api/admin/categories/{category_pk}/products/{product_pk/
admin_category_router.register('products', AdminProductOfCategoryViewSet, basename='admin-products-category')

# api/admin/subcategories/{subcategory_pk}/products and api/admin/subcategories/{subcategory_pk}/products/{product_pk/
admin_sub_category_router.register('products', AdminProductOfSubCategoryViewSet, basename='admin-products-sub-category')

# ========> Fin d'enregistrement des URLs de dépendance

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/', include(store_router.urls)),
    path('api/', include(admin_store_router.urls)),
    path('api/', include(sub_category_router.urls)),
    path('api/', include(admin_sub_category_router.urls)),
    path('api/', include(category_router.urls)),
    path('api/', include(admin_category_router.urls)),
]
