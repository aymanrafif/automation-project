from modules.library_item import LibraryItem

class CD(LibraryItem):
    def __init__(self, title, subject, upc, artist):
        LibraryItem.__init__(self, title, subject)
        self.artist = artist