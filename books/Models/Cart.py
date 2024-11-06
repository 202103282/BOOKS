class Cart:
    """Represents a shopping cart for a customer, allowing management of items."""

    def __init__(self, customer):
        self._items = []
        self._customer = customer
        self._cart_id = None
        self._created_date = None

    # Getters
    def get_items(self):
        return self._items

    def get_customer(self):
        return self._customer

    def get_cart_id(self):
        return self._cart_id

    def get_created_date(self):
        return self._created_date

    # Setters
    def set_items(self, items):
        self._items = items

    def set_customer(self, customer):
        self._customer = customer

    def set_cart_id(self, cart_id):
        self._cart_id = cart_id

    def set_created_date(self, created_date):
        self._created_date = created_date

    def add_item(self, ebook, quantity):
        """Adds an ebook as an item in the cart."""
        self._items.append(OrderItem(ebook, quantity, ebook.get_price(), Decimal(0)))

    def remove_item(self, order_item):
        """Removes an item from the cart."""
        self._items.remove(order_item)

    def calculate_cart_total(self):
        """Calculates the total price of all items in the cart."""
        return sum(item.final_price() for item in self._items)

    def __str__(self):
        return f"Cart(total={self.calculate_cart_total()})"
