import json
from models import Author, Quote, connect


# Завантажуємо авторів
with open('authors.json', 'r', encoding='utf-8') as f:
    authors = json.load(f)

for author in authors:
    a = Author(
        fullname=author.get('fullname'),
        born_date=author.get('born_date'),
        born_location=author.get('born_location'),
        description=author.get('description')
    )
    a.save()

# Завантажуємо цитати
with open('qoutes.json', 'r', encoding='utf-8') as f:
    quotes = json.load(f)

for quote in quotes:
    author_name = quote.get('author')
    author_obj = Author.objects(fullname=author_name).first() # type: ignore
    if author_obj:
        q = Quote(
            tags=quote.get('tags', []),
            author=author_obj,
            quote=quote.get('quote')
        )
        q.save()