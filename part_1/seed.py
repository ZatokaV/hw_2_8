import json
from models import Quotes, Authors


with open("authors.json", 'r', encoding='utf-8') as authors:
    authors_data = json.load(authors)

with open('quotes.json', 'r', encoding='utf-8') as quotes:
    quotes_data = json.load(quotes)


for el in authors_data:
    record = Authors(fullname=el['fullname'],
                     born_date=el['born_date'],
                     born_location=el['born_location'],
                     description=el['description'])
    record.save()


def change_name_to_id(name):
    temp_list = []
    authors = Authors.objects()

    for author in authors:
        author_and_id = {author.id: author.fullname}
        temp_list.append(author_and_id)

    for el in temp_list:
        for key, value in el.items():
            if value == name:
                return key
    return name


for el in quotes_data:
    record = Quotes(tags=el['tags'],
                    author=change_name_to_id(el['author']),
                    quote=el['quote']).save()
    record.save()
