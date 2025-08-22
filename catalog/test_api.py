from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Brand, Product

class APITestCase(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        
        # Create test category and brand
        self.category = Category.objects.create(
            name="Electronics",
            description="Electronic devices"
        )
        self.brand = Brand.objects.create(
            name="Apple",
            website="https://apple.com",
            country="USA"
        )
        
        # Create test product
        self.product = Product.objects.create(
            name="iPhone 15",
            description="Latest iPhone",
            price=999.99,
            category=self.category,
            brand=self.brand,
            sku="IPHONE15-001"
        )

    def test_get_products_list(self):
        """Test GET /api/products/"""
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_detail(self):
        """Test GET /api/products/1/"""
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'iPhone 15')

    def test_create_product(self):
        """Test POST /api/products/"""
        url = reverse('product-list')
        data = {
            'name': 'Galaxy S24',
            'description': 'Samsung phone',
            'price': 899.99,
            'category': self.category.id,
            'brand': self.brand.id,
            'sku': 'GALAXY-S24-001'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_update_product(self):
        """Test PUT /api/products/1/"""
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        data = {
            'name': 'iPhone 15 Pro',
            'description': 'Updated description',
            'price': 1199.99,
            'category': self.category.id,
            'brand': self.brand.id,
            'sku': 'IPHONE15-001'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'iPhone 15 Pro')

    def test_delete_product(self):
        """Test DELETE /api/products/1/"""
        url = reverse('product-detail', kwargs={'pk': self.product.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)