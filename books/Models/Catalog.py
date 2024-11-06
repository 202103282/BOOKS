from ebook import Ebook

class Catalog:
    """Manages a collection of ebooks with functionalities to add, remove, and search."""

    def __init__(self):
        self._ebooks = []
        self._catalog_name = ""
        self._created_date = ""
        self._last_updated = ""

    # Getters
    def get_ebooks(self):
        return self._ebooks

    def get_catalog_name(self):
        return self._catalog_name

    def get_created_date(self):
        return self._created_date

    def get_last_updated(self):
        return self._last_updated

    # Setters
    def set_ebooks(self, ebooks):
        self._ebooks = ebooks

    def set_catalog_name(self, catalog_name):
        self._catalog_name = catalog_name

    def set_created_date(self, created_date):
        self._created_date = created_date

    def set_last_updated(self, last_updated):
        self._last_updated = last_updated

    def add_ebook(self, ebook: Ebook):
        """Adds an ebook to the catalog."""
        self._ebooks.append(ebook)
        self.set_last_updated("Date when last updated")

    def remove_ebook(self, ebook: Ebook):
        """Removes an ebook from the catalog."""
        self._ebooks.remove(ebook)
        self.set_last_updated("Date when last updated")

    def search_ebook(self, criteria: str):
        """Searches for ebooks that match the criteria in title, author, or genre."""
        return [ebook for ebook in self._ebooks if criteria.lower() in (ebook.get_title().lower() + ebook.get_author().lower() + ebook.get_genre().lower())]

    def __str__(self):
        return f"Catalog({len(self._ebooks)} ebooks, name={self._catalog_name})"
