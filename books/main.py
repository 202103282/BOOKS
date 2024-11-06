import unittest
from decimal import Decimal
from datetime import date
from customer import Customer
from ebook import Ebook
from catalog import Catalog
from cart import Cart
from order import Order
from order_item import OrderItem
from invoice import Invoice


class TestEBookStore(unittest.TestCase):

    def setUp(self):
        """Set up test fixtures."""
        self.catalog = Catalog()
        self.customer = Customer(email="test@example.com", password="password", name="Test User", phone="123-456-7890")
        self.ebook = Ebook(title="Test E-Book", author="Author Name", publication_date=date.today(), genre="Fiction",
                           price=Decimal("9.99"))
        self.cart = Cart(customer=self.customer)

        # Add an ebook to the catalog
        self.catalog.add_ebook(self.ebook)

    def test_add_ebook_to_catalog(self):
        """Test adding an ebook to the catalog."""
        self.assertIn(self.ebook, self.catalog._ebooks)

    def test_remove_ebook_from_catalog(self):
        """Test removing an ebook from the catalog."""
        self.catalog.remove_ebook(self.ebook)
        self.assertNotIn(self.ebook, self.catalog._ebooks)

    def test_search_ebook_in_catalog(self):
        """Test searching for an ebook in the catalog."""
        result = self.catalog.search_ebook("Test E-Book")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_title(), "Test E-Book")

    def test_create_customer_account(self):
        """Test creating a new customer account."""
        self.assertEqual(self.customer.get_name(), "Test User")
        self.assertEqual(self.customer.email, "test@example.com")

    def test_modify_customer_details(self):
        """Test modifying customer details."""
        self.customer.set_name("Updated User")
        self.assertEqual(self.customer.get_name(), "Updated User")

    def test_add_ebook_to_cart(self):
        """Test adding an ebook to the shopping cart."""
        self.cart.add_item(self.ebook, 2)
        self.assertEqual(len(self.cart._items), 1)

    def test_remove_ebook_from_cart(self):
        """Test removing an ebook from the shopping cart."""
        order_item = OrderItem(self.ebook, 1, self.ebook.price, Decimal(0))
        self.cart.add_item(self.ebook, 1)
        self.cart.remove_item(order_item)
        self.assertEqual(len(self.cart._items), 0)

    def test_calculate_cart_total(self):
        """Test calculating the total price of the cart."""
        self.cart.add_item(self.ebook, 2)
        total = self.cart.calculate_cart_total()
        self.assertEqual(total, self.ebook.price * 2)

    def test_create_order_from_cart(self):
        """Test creating an order from the cart."""
        self.cart.add_item(self.ebook, 2)
        order = Order(order_date=date.today())
        for item in self.cart._items:
            order.add_item(item)
        self.assertEqual(len(order.items), 1)

    def test_generate_invoice(self):
        """Test generating an invoice."""
        self.cart.add_item(self.ebook, 2)
        order = Order(order_date=date.today())
        for item in self.cart._items:
            order.add_item(item)
        invoice = Invoice(invoice_id="INV123", order=order)
        self.assertIn("Invoice ID: INV123", str(invoice))


if __name__ == "__main__":
    unittest.main()
