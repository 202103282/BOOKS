# Ebook

class Ebook:
    """Represent an e-book in the catalog."""

    def __init__(self, title, author, publication_date, genre, price):
        """Initialize e-book details."""
        self.__title = title
        self.__author = author
        self.__publication_date = publication_date
        self.__genre = genre
        self.__price = price

    # Getters
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_publication_date(self):
        return self.__publication_date

    def get_genre(self):
        return self.__genre

    def get_price(self):
        return self.__price

    # Setters
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_publication_date(self, publication_date):
        self.__publication_date = publication_date

    def set_genre(self, genre):
        self.__genre = genre

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        """Return a string representation of the e-book."""
        return f"{self.__title} by {self.__author}, {self.__genre} - ${self.__price:.2f}"
