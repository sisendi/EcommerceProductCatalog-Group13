from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.shortcuts import render, get_object_or_404
from .models import Category, Brand, Product, ProductImage, Review
from .serializers import (
    CategorySerializer, BrandSerializer, ProductSerializer,
    ProductImageSerializer, ReviewSerializer
)

# API Views (existing)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = [AllowAny]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]


# Frontend Views (new)
def home_view(request):
    """Homepage view"""
    products = Product.objects.filter(is_active=True)[:6]  # Show first 6 active products
    categories = Category.objects.all()
    return render(request, 'catalog/home.html', {
        'products': products,
        'categories': categories
    })


def product_list_view(request):
    """Frontend view to display all products"""
    products = Product.objects.filter(is_active=True)
    return render(request, 'catalog/product_list.html', {'products': products})


def product_detail_view(request, pk):
    """Frontend view to display single product"""
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    images = product.images.all()
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'images': images
    })


def category_list_view(request):
    """Frontend view to display all categories"""
    categories = Category.objects.all()
    return render(request, 'catalog/category_list.html', {'categories': categories})


def category_products_view(request, pk):
    """Frontend view to display products in a category"""
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category, is_active=True)
    return render(request, 'catalog/category_products.html', {
        'category': category,
        'products': products
    })