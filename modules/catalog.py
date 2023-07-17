from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import DVD

class Catalog():

    def __init__(self, catalog = None):
        self.catalog = catalog


    def search(self, input_search):
        list_result = []
        for catalog in self.catalog:
            for item in catalog:
                if input_search in item.title.lower():
                    if type(item) in [Magazine]:
                        list_result.append('\nTitle:' + item.title+
                            '\nVolume:' + item.volume+
                            '\nIssue:' + item.issue)
                    elif type(item) in [Book]:
                        list_result.append('\nTitle:' + item.title+
                            '\nISSBN:' + item.issbn+
                            '\nAuthors:' + item.authors+
                            '\nDDS Number:' + item.dds_number)
                    elif type(item) in [DVD]:
                        list_result.append('\nTitle:' + item.title+
                            '\nActors:' + item.actors+
                            '\nDirectors:' + item.directors+
                            '\nGenre:' +  item.genre)
                    else:
                        pass
        return list_result