from modules.library_item import LibraryItem

class Author():
    name = None

class Book(LibraryItem):
    def __init__(self, title, subject, upc, issbn, authors, dds_number):
        LibraryItem.__init__(self, title, subject) # Harus tambahin self dalam constructor
        self.issbn = issbn
        self.authors = authors
        self.dds_number = dds_number