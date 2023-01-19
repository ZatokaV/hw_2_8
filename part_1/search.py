from models import Quotes


def pars_input(query) -> dict:
    list_args = query.split(':')
    field = list_args[0]
    value = list_args[-1].strip().split(',')
    return {field: value}


def find_quotes_to_name(query_dict):
    author_name = ''
    all_quotes = []

    quotes = Quotes.objects()
    for quote in quotes:
        if quote.author.fullname.capitalize() == query_dict['name'][0].capitalize(
        ) or quote.author.fullname.capitalize().startswith(query_dict['name'][0].capitalize()):
            author_name = quote.author.fullname
            all_quotes.append(quote.quote)

    print(f'All quotes by {author_name}: {all_quotes}')


def find_quote_to_tag(query_dict):
    all_quotes = []
    quotes = Quotes.objects()
    for quote in quotes:
        for tag in quote.tags:
            for part_tag in query_dict['tag']:
                if tag.startswith(part_tag):
                    all_quotes.append(f'Quote by {quote.author.fullname} with tag {tag}: {quote.quote}')
    for result in all_quotes:
        print(result)


def find_quotes_to_tags(query_dict):
    all_quotes = []
    quotes = Quotes.objects()
    for quote in quotes:
        for tag in quote.tags:
            for part_tag in query_dict['tags']:
                if tag.startswith(part_tag):
                    all_quotes.append(f'Quote by {quote.author.fullname} with tag {tag}: {quote.quote}')
    for result in all_quotes:
        print(result)


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
            find_quote_to_tag(query_dict)
        if 'tags' in query_dict:
            find_quotes_to_tags(query_dict)
