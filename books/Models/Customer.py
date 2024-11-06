from account import Account
from order import Order
from ebook import Ebook
from invoice import Invoice
from order_item import OrderItem
from decimal import Decimal
from datetime import date


class Customer(Account):
    """Represents a customer with personal details and order management capabilities, inheriting from Account for authentication."""

    def __init__(self, email: str, password: str, name: str, phone: str, loyalty_member: bool = False):
        # Initialize the parent class (Account) with email and password
        super().__init__(email, password)

        # Initialize additional Customer-specific attributes
        self._name = name
        self._phone = phone
        self._loyalty_member = loyalty_member
        self._orders = []

    # Getters
    def get_name(self):
        return self._name

    def get_phone(self):
        return self._phone

    def get_loyalty_member(self):
        return self._loyalty_member

    def get_orders(self):
        return self._orders

    # Setters
    def set_name(self, name: str):
        self._name = name

    def set_phone(self, phone: str):
        self._phone = phone

    def set_loyalty_member(self, loyalty_member: bool):
        self._loyalty_member = loyalty_member

    def set_orders(self, orders: list):
        self._orders = orders

    def create_order(self, order: Order):
        """Creates a new order for the customer."""
        self._orders.append(order)

    def view_orders(self):
        """Returns a list of the customer's orders."""
        return self._orders

    def purchase_ebook(self, ebook: Ebook) -> Invoice:
        """Purchases an ebook and returns an invoice for the purchase."""
        # Create a new order and add an item for the purchased ebook
        order = Order(order_date=date.today())
        order_item = OrderItem(ebook, 1, ebook.get_price(), Decimal(0))
        order.add_item(order_item)

        # Store the order in the customer's order history
        self.create_order(order)

        # Generate an invoice for the order
        invoice = Invoice(invoice_id="123", order=order)
        return invoice

    def __str__(self):
        return f"Customer(name={self._name}, email={self.get_email()}, loyalty_member={self._loyalty_member})"
