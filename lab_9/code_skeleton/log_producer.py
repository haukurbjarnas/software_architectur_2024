import string
import time
import random

# TODO: RabbitMQ connection logic goes here
import pika
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", credentials=pika.PlainCredentials("guest", "guest")
    )
)
channel = connection.channel()

channel.exchange_declare(exchange="hello-world", exchange_type="fanout")




def random_log() -> str:
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


while True:
    log_entry = random_log()
    print(f'Publishing log: {log_entry}')
    # TODO: publish logs
    channel.basic_publish(exchange="hello-world", routing_key="", body=log_entry)
    time.sleep(3)



