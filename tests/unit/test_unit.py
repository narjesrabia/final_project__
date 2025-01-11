from django.test import TestCase
from django.contrib.auth.models import User
from base.models import Product, Review, Order, OrderItem, ShippingAddress


class ProductModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.product = Product.objects.create(
            user=self.user,
            name="Test Product",
            brand="Test Brand",
            price=19.99
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.brand, "Test Brand")
        self.assertEqual(self.product.price, 19.99)

    def test_product_str_method(self):
        self.assertEqual(str(self.product), "Test Product | Test Brand | 19.99")

class ReviewModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.product = Product.objects.create(
            user=self.user,
            name="Test Product",
            brand="Test Brand",
            price=19.99
        )
        self.review = Review.objects.create(
            product=self.product,
            user=self.user,
            rating=5,
            comment="Great product!"
        )

    def test_review_creation(self):
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "Great product!")

    def test_review_str_method(self):
        self.assertEqual(str(self.review), "5")

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod="Credit Card",
            totalPrice=100.00,
            isPaid=True
        )

    def test_order_creation(self):
        self.assertEqual(self.order.paymentMethod, "Credit Card")
        self.assertEqual(self.order.totalPrice, 100.00)
        self.assertTrue(self.order.isPaid)

    def test_order_str_method(self):
        self.assertEqual(str(self.order), str(self.order.createdAt))

class OrderItemModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.product = Product.objects.create(
            user=self.user,
            name="Test Product",
            brand="Test Brand",
            price=19.99
        )
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod="Credit Card",
            totalPrice=100.00,
            isPaid=True
        )
        self.order_item = OrderItem.objects.create(
            product=self.product,
            order=self.order,
            name="Test Product",
            qty=2,
            price=19.99
        )

    def test_order_item_creation(self):
        self.assertEqual(self.order_item.qty, 2)
        self.assertEqual(self.order_item.price, 19.99)

    def test_order_item_str_method(self):
        self.assertEqual(str(self.order_item), "Test Product")

class ShippingAddressModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.order = Order.objects.create(
            user=self.user,
            paymentMethod="Credit Card",
            totalPrice=100.00,
            isPaid=True
        )
        self.shipping_address = ShippingAddress.objects.create(
            order=self.order,
            address="123 Test St.",
            city="Test City",
            postalCode="12345",
            country="Test Country",
            shippingPrice=5.00
        )

    def test_shipping_address_creation(self):
        self.assertEqual(self.shipping_address.address, "123 Test St.")
        self.assertEqual(self.shipping_address.city, "Test City")
        self.assertEqual(self.shipping_address.shippingPrice, 5.00)

    def test_shipping_address_str_method(self):
        self.assertEqual(str(self.shipping_address), "123 Test St.")
