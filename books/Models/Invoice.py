from decimal import Decimal
from order import Order

class Invoice:
    """Generates and represents an invoice for an order, including VAT calculation and discounts."""

    def __init__(self, invoice_id: str, order: Order, VAT_rate: Decimal = Decimal(0.08), discount: Decimal = Decimal(0.0)):
        self._invoice_id = invoice_id
        self._order = order
        self._VAT_rate = VAT_rate
        self._discount = discount  # New attribute representing any discounts applied

    # Getters
    def get_invoice_id(self):
        return self._invoice_id

    def get_order(self):
        return self._order

    def get_VAT_rate(self):
        return self._VAT_rate

    def get_discount(self):
        return self._discount

    # Setters
    def set_invoice_id(self, invoice_id: str):
        self._invoice_id = invoice_id

    def set_order(self, order: Order):
        self._order = order

    def set_VAT_rate(self, VAT_rate: Decimal):
        self._VAT_rate = VAT_rate

    def set_discount(self, discount: Decimal):
        self._discount = discount

    def calculate_VAT(self):
        """Calculates the VAT based on the order's total amount."""
        return self._order.calculate_total() * self._VAT_rate

    def generate_invoice(self):
        """Generates a string representation of the invoice details."""
        total_amount = self._order.calculate_total() - self._discount
        total_with_VAT = total_amount + self.calculate_VAT()
        return f"Invoice ID: {self._invoice_id}\nTotal: {total_amount}\nTotal with VAT: {total_with_VAT}"

    def __str__(self):
        return self.generate_invoice()
