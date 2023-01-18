from models import Authors, Quotes


def pars_input(query):
    list_args = query.split(':')
    field = list_args[0]
    value = list_args[-1].strip().split(',')
    return {field: value}


def find_quotes_to_name(query_dict):
    author_name = ''
    all_quotes = []

    authors = Authors.objects()
    for author in authors:
        if author.fullname.capitalize() == query_dict['name'][0].capitalize(
        ) or author.fullname.capitalize().startswith(query_dict['name'][0].capitalize()):
            author_name = author.fullname
    quotes = Quotes.objects()
    for quote in quotes:
        if quote.author.fullname.capitalize() == query_dict['name'][0].capitalize(
        ) or quote.author.fullname.capitalize().startswith(query_dict['name'][0].capitalize()):
            all_quotes.append(quote.quote)
    if len(all_quotes) == 0:
        all_quotes = str("Author's quotes not found")

    print(author_name, all_quotes)


search = True

while search:
    query = input("Ready to search... ")

    if query == "exit":
        search = False

    else:

        query_dict = pars_input(query)

        if 'name' in query_dict:
            find_quotes_to_name(query_dict)
        if 'tag' in query_dict:
            print(query_dict['tag'])
        if 'tags' in query_dict:
            print(query_dict['tags'])
