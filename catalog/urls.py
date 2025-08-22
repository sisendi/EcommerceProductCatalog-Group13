from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CategoryViewSet, BrandViewSet, ProductViewSet,
    ProductImageViewSet, ReviewViewSet,
    home_view, product_list_view, product_detail_view,
    category_list_view, category_products_view
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list_view, name='product-list-frontend'),
    path('products/<int:pk>/', product_detail_view, name='product-detail-frontend'),
    path('categories/', category_list_view, name='category-list-frontend'),
    path('categories/<int:pk>/', category_products_view, name='category-products'),
    
    path('api/', include(router.urls)),
]