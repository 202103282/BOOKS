class Discount:
    @staticmethod
    def apply_loyalty_discount(amount):
        return amount * 0.1  # 10% discount

    @staticmethod
    def apply_bulk_discount(amount):
        return amount * 0.2  # 20% discount for bulk orders
