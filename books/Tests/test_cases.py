from EBook import EBook
from Customer import Customer
from ShoppingCart import ShoppingCart
from Order import Order
from Invoice import Invoice

def test_ebook_management():
    ebook = EBook("Python Programming", "John Wick", "2023-10-12", "Programming", 29.99)
    print(ebook)

def test_customer_management():
    customer = Customer("Alice Kim", "alicekim@gmail.com", True)
    print(customer)

def test_shopping_cart():
    ebook1 = EBook("Data Science", "Jane Harris", "2022-08-11", "Science", 25.00)
    ebook2 = EBook("Art for Everyone", "Albert Johnson", "2023-05-18", "Technology", 20.00)
    cart = ShoppingCart()
    cart.add_to_cart(ebook1, 2)
    cart.add_to_cart(ebook2, 3)
    print(cart)
    print("Total:", cart.get_total())

def test_order_invoice():
    customer = Customer("Alice Kim", "alicekim@gmail.com", True)
    ebook1 = EBook("Data Science", "Jane Harris", "2022-08-11", "Science", 25.00)
    ebook2 = EBook("Art for Everyone", "Albert Johnson", "2023-05-18", "Technology", 20.00)
    cart = ShoppingCart()
    cart.add_to_cart(ebook1, 5)
    order = Order(customer, cart, "2024-10-31")
    order.apply_discount()
    invoice = Invoice(order)
    invoice.generate_invoice()

if __name__ == "__main__":
    print("Testing EBook Management:")
    test_ebook_management()
    print("\nTesting Customer Management:")
    test_customer_management()
    print("\nTesting Shopping Cart:")
    test_shopping_cart()
    print("\nTesting Order and Invoice Generation:")
    test_order_invoice()
