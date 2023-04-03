from django.contrib import admin
from django.urls import path, include
from stores.views import *
from rest_framework_nested import routers

router = routers.SimpleRouter()

# ========> Enregistrement des URLs de base

# api/stores/ and api/stores/{store_pk}/
router.register('stores', StoreViewSet, basename='stores')

# api/categories/ and api/categories/{category_pk}/
router.register('categories', CategoryViewSet, basename='categories')

# api/subcategories/ and api/subcategories/{subcategory_pk}/
router.register('subcategories', SubCategoryViewSet, basename='sub-categories')

# api/products/ and api/products/{product_pk}/
router.register('products', ProductViewSet, basename='products')

# api/admin/stores/ and api/admin/stores/{store_pk}/
router.register('admin/stores', AdminStoreViewSet, basename='admin-stores')

# api/admin/categories/ and api/admin/categories/{category_pk}/
router.register('admin/categories', AdminCategoryViewSet, basename='admin-categories')

# api/admin/subcategories/ and api/admin/subcategories/{subcategory_pk}/
router.register('admin/subcategories', AdminSubCategoryViewSet, basename='admin-sub-categories')

# api/admin/products/ and api/admin/products/{product_pk}/
router.register('admin/products', AdminProductViewSet, basename='admin-products')

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
