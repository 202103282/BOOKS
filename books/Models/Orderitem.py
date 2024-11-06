from ebook import Ebook
from decimal import Decimal


class OrderItem:
    """Represents an item in an order, including quantity, price, discount, and the associated Ebook."""

    def __init__(self, ebook: Ebook, quantity: int, price: Decimal, discount: Decimal):
        self._ebook = ebook
        self._quantity = quantity
        self._price = price
        self._discount = discount

    # Getters
    def get_ebook(self):
        return self._ebook

    def get_quantity(self):
        return self._quantity

    def get_price(self):
        return self._price

    def get_discount(self):
        return self._discount

    # Setters
    def set_ebook(self, ebook: Ebook):
        self._ebook = ebook

    def set_quantity(self, quantity: int):
        if quantity > 0:
            self._quantity = quantity
        else:
            raise ValueError("Quantity must be greater than zero.")

    def set_price(self, price: Decimal):
        if price >= 0:
            self._price = price
        else:
            raise ValueError("Price must be non-negative.")

    def set_discount(self, discount: Decimal):
        if 0 <= discount <= 1:
            self._discount = discount
        else:
            raise ValueError("Discount must be between 0 and 1.")

    def final_price(self):
        """Calculates the price after discount for this item."""
        return self._price * (1 - self._discount) * self._quantity

    def __str__(self):
        return f"OrderItem(ebook={self._ebook}, quantity={self._quantity}, final_price={self.final_price()})"
