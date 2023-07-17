from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import DVD
from modules.catalog import Catalog

import json

book1 = Book(
    'Title Test',
    'Ini subject test',
    None,
    '1234-5647',
    'Singgih',
    '789456789'
)

book2 = Book(
    'Harry Potter 2',
    'Ini subject dari buku Harry Potter 2',
    None,
    '3216-7895',
    'Wawan',
    '963258741'
)

book3 = Book(
    'Harry Potter 9',
    'Ini subject test',
    None,
    '1234-5647',
    'Singgih',
    '789456789'
)

magazine1 = Magazine(
    'Media Kompas',
    'Edisi 17 Juli 2023',
    None,
    'Volume 22',
    'Issue 3'
)

magazine2 = Magazine(
    'Media CNN',
    'Edisi 12 Juli 2023',
    None,
    'Volume 1',
    'Issue 2'
)

dvd1 = DVD(
    'DVD 1',
    'Ini subject DVD 1',
    None,
    'Morgan Freeman',
    'Pak Director A',
    'Comedy'
)

# Collect data per jenis
books = [book1, book2, book3]
magazines = [magazine1, magazine2]
dvds = [dvd1]

# Collect all data
catalog_all = [books, magazines, dvds]

# Get data from json
f = open('catalog.json')
data_json = json.load(f)

# Collect data from json
for item in data_json:
    if item['source'] == 'book':
        books.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc = item['upc'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number']
        ))
    elif item['source'] == 'magazine':
        magazines.append(Magazine(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            volume = item['volume'],
            issue = item['issue']
        ))
    else:
        pass

# Input Search
input_search = 'MEDIA'
results = Catalog(catalog_all).search(input_search.lower())

if results:
    for i, result in enumerate(results):
        print(f'RESULT-{i+1} | {result}\n')
else:
    print('No Result')

# for catalog in catalog_all:
#     for item in catalog:
#         if input_search in item.title.lower():
#             if type(item) in [Magazine]:
#                 print('\nTitle:', item.title,
#                       '\nCategory: Magazine',
#                       '\nVolume:', item.volume,
#                       '\nIssue:', item.issue)
#             elif type(item) in [Book]:
#                 print('\nTitle:', item.title,
#                       '\nCategory: Book',
#                       '\nISSBN:', item.issbn,
#                       '\nAuthors:', item.authors,
#                       '\nDDS Number:', item.dds_number)
#             elif type(item) in [DVD]:
#                 print('\nTitle:', item.title,
#                       '\nCategory: DVD',
#                       '\nActors:', item.actors,
#                       '\nDirectors:', item.directors,
#                       '\nGenre:', item.genre)
