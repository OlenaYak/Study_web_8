from faker import Faker
import pika
from models import connect_db, Contact


connect_db()

fake = Faker()

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

N = 10  # кіл-ть контактів

for _ in range(N):
    contact = Contact(
        fullname=fake.name(),
        email=fake.email()
    ).save()
    contact_id = str(contact.id)
    channel.basic_publish(exchange='', routing_key='email_queue', body=contact_id)
    print(f" [x] Sent contact id {contact_id}")

connection.close()