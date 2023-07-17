from modules.library_item import LibraryItem

class DVD(LibraryItem):
    def __init__(self, title, subject, upc, actors, directors, genre):
        LibraryItem.__init__(self, title, subject) # Harus tambahin self dalam constructor
        self.actors = actors
        self.directors = directors
        self.genre = genre