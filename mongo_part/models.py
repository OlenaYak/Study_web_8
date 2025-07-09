from mongoengine import Document, StringField, ListField, ReferenceField, connect

connect(db="web25", host="mongodb+srv://userweb25:567234@clusterolena.onftjc3.mongodb.net/?retryWrites=true&w=majority&appName=ClusterOlena")

class Author(Document):
    fullname = StringField(required=True, max_length=120)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=200)
    description = StringField()

    # meta = {'collection': 'autors'}


class Quote(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)

    # meta = {'collection': 'quotes'}