import pika
from models import Contact, connect_db


connect_db()

def send_email_stub(contact):
    print(f"Sending email to {contact.fullname} ({contact.email})")
    # тут нічого не робимо

def callback(ch, method, properties, body):
    contact_id = body.decode()
    contact = Contact.objects(id=contact_id).first() # type: ignore
    if contact:
        send_email_stub(contact)
        contact.update(message_sent=True)
        print(f" [x] Email sent and updated for contact id {contact_id}")
    else:
        print(f" [!] Contact not found for id {contact_id}")

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='email_queue')

channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()