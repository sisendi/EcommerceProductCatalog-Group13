# E-commerce Product Catalog API

## Group Member
- 147115 Serena Isendi
- 169915 Joy Warigi
  

## Project Description
Django REST API for managing an e-commerce product catalog with CRUD operations for products, categories, brands, images, and reviews.

## Models (5 Models)

1. **Category** - Product categories (Electronics, Clothing, etc.)
   - Fields: name, description, created_at
   - Relationships: One-to-Many with Products

2. **Brand** - Product manufacturers
   - Fields: name, website, country  
   - Relationships: One-to-Many with Products

3. **Product** - Main product information
   - Fields: name, description, price, category, brand, sku, is_active, created_at
   - Relationships: Many-to-One with Category/Brand, One-to-Many with Images/Reviews

4. **ProductImage** - Product images
   - Fields: product, image_url, alt_text, is_primary
   - Relationships: Many-to-One with Product

5. **Review** - Customer reviews
   - Fields: product, reviewer_name, rating, comment, created_at
   - Relationships: Many-to-One with Product

## Serializers (5 Serializers)

- **CategorySerializer** - Complete category serialization
- **BrandSerializer** - Complete brand serialization  
- **ProductSerializer** - Product serialization with validation (price > 0), includes nested images/reviews
- **ProductImageSerializer** - Product image serialization
- **ReviewSerializer** - Review serialization with validation (rating 1-5)

## Views/Viewsets (5 ViewSets)

All implemented using Django REST Framework's `ModelViewSet` providing full CRUD operations:
- **CategoryViewSet** - `/api/categories/`
- **BrandViewSet** - `/api/brands/`
- **ProductViewSet** - `/api/products/`
- **ProductImageViewSet** - `/api/product-images/`
- **ReviewViewSet** - `/api/reviews/`

Permissions: AllowAny (for development/testing)

## URL Patterns

RESTful URLs using DRF's DefaultRouter:
```
/api/categories/          # GET, POST
/api/categories/{id}/     # GET, PUT, DELETE
/api/brands/              # GET, POST  
/api/brands/{id}/         # GET, PUT, DELETE
/api/products/            # GET, POST
/api/products/{id}/       # GET, PUT, DELETE
/api/product-images/      # GET, POST
/api/product-images/{id}/ # GET, PUT, DELETE
/api/reviews/             # GET, POST
/api/reviews/{id}/        # GET, PUT, DELETE
```

## Testing Results

**Test Framework**: Django's built-in testing framework

**Test Output**:
```
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.036s
OK
Destroying test database for alias 'default'...
```
<img width="594" height="142" alt="Screenshot 2025-08-22 at 21 08 36" src="https://github.com/user-attachments/assets/b2912503-620b-41c3-be5f-7fa9d37f3517" />


**Test Cases**:
1. GET /api/products/ - List products (200 OK)
2. GET /api/products/{id}/ - Get specific product (200 OK)
3. POST /api/products/ - Create product (201 Created)
4. PUT /api/products/{id}/ - Update product (200 OK)
5. DELETE /api/products/{id}/ - Delete product (204 No Content)

**All tests passed** - CRUD operations working correctly for all HTTP methods.

