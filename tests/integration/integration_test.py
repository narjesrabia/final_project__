import pytest
import json
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from base.models import Product, User, Review
from django.contrib.auth.models import User

class ProductIntegrationTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser('admin', 'admin@test.com', 'password')
        self.regular_user = User.objects.create_user('user', 'user@test.com', 'password')
        
        self.product1 = Product.objects.create(
            name="Product 1", price=100, brand="Brand A", countInStock=10,
            category="Category A", description="Description 1"
        )
        self.product2 = Product.objects.create(
            name="Product 2", price=200, brand="Brand B", countInStock=5,
            category="Category B", description="Description 2", rating=4.5
        )
        
        self.client = APIClient()

    def test_get_all_products(self):
        """Test retrieving all products."""
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['products']), 2)

    def test_get_top_products(self):
        """Test retrieving top-rated products."""
        response = self.client.get('/api/products/top/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Product 2")

    def test_get_single_product(self):
        """Test retrieving a single product by ID."""
        response = self.client.get(f'/api/products/{self.product1._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Product 1")

    def test_create_product_as_admin(self):
        """Test creating a product as an admin."""
        self.client.force_authenticate(user=self.admin_user)
        payload = {
            "name": "Product 3",
            "price": 300,
            "brand": "Brand C",
            "countInStock": 15,
            "category": "Category C",
            "description": "Description 3",
        }
        response = self.client.post('/api/products/create/', payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 3)

    def test_create_product_as_regular_user(self):
        """Test creating a product as a regular user."""
        self.client.force_authenticate(user=self.regular_user)
        payload = {
            "name": "Product 3",
            "price": 300,
            "brand": "Brand C",
            "countInStock": 15,
            "category": "Category C",
            "description": "Description 3",
        }
        response = self.client.post('/api/products/create/', payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_product_as_admin(self):
        """Test deleting a product as an admin."""
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.delete(f'/api/products/delete/{self.product1._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)

    def test_delete_product_as_regular_user(self):
        """Test deleting a product as a regular user."""
        self.client.force_authenticate(user=self.regular_user)
        response = self.client.delete(f'/api/products/delete/{self.product1._id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
