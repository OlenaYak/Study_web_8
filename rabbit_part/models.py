from mongoengine import connect, disconnect, Document, StringField, BooleanField

def connect_db():
    disconnect(alias='default')
    connect(db="web25", host="mongodb+srv://userweb25:*****@clusterolena.onftjc3.mongodb.net/?retryWrites=true&w=majority&appName=ClusterOlena")


class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)
