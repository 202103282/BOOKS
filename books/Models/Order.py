from datetime import date
from decimal import Decimal
from order_item import OrderItem

class Order:
    """Represents a customer's order, containing multiple items and handling total and discount calculations."""

    def __init__(self, order_id: str, customer_name: str, order_date: date, status: str):
        self._order_id = order_id
        self._customer_name = customer_name
        self._order_date = order_date
        self._status = status  # New attribute to track the status of the order (e.g., "Processing", "Shipped")
        self._items = []  # List to hold OrderItem instances

    # Getters
    def get_order_id(self):
        return self._order_id

    def get_customer_name(self):
        return self._customer_name

    def get_order_date(self):
        return self._order_date

    def get_status(self):
        return self._status

    def get_items(self):
        return self._items

    # Setters
    def set_order_id(self, order_id: str):
        self._order_id = order_id

    def set_customer_name(self, customer_name: str):
        self._customer_name = customer_name

    def set_order_date(self, order_date: date):
        self._order_date = order_date

    def set_status(self, status: str):
        self._status = status

    def set_items(self, items: list):
        self._items = items

    def add_item(self, item: OrderItem):
        """Adds an item to the order."""
        self._items.append(item)

    def remove_item(self, item: OrderItem):
        """Removes an item from the order."""
        self._items.remove(item)

    def calculate_total(self):
        """Calculates the total cost for all items in the order."""
        return sum(item.final_price() for item in self._items)

    def __str__(self):
        return f"Order(order_id={self._order_id}, customer_name={self._customer_name}, date={self._order_date}, status={self._status}, total={self.calculate_total()})"
