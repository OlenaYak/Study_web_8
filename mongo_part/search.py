from models import Author, Quote, connect

def search_by_author(name):
    author = Author.objects(fullname=name).first() # type: ignore
    if author:
        quotes = Quote.objects(author=author) # type: ignore
        for q in quotes:
            print(q.quote.encode('utf-8').decode())
    else:
        print("Автор не знайдений.")

def search_by_tag(tag):
    quotes = Quote.objects(tags=tag) # type: ignore
    for q in quotes:
        print(q.quote.encode('utf-8').decode())

def search_by_tags(tags_list):
    quotes = Quote.objects(tags__in=tags_list) # type: ignore
    for q in quotes:
        print(q.quote.encode('utf-8').decode())

def main():
    while True:
        command = input("Введіть команду: ")
        if command == 'exit':
            break
        try:
            key, value = command.split(':', 1)
            if key == 'name':
                search_by_author(value.strip())
            elif key == 'tag':
                search_by_tag(value.strip())
            elif key == 'tags':
                tags = value.strip().split(',')
                search_by_tags(tags)
            else:
                print("Невідома команда.")
        except ValueError:
            print("Неправильний формат команди. Використовуйте: команда:значення")

if __name__ == '__main__':
    main()