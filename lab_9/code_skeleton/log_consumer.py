
# TODO: You need to implement the consumption logic and connection to RabbitMQ here.
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", credentials=pika.PlainCredentials("guest", "guest")))
channel = connection.channel()
channel.exchange_declare(exchange="hello-world", exchange_type="fanout")
channel.queue_declare(queue="hello-consumer")
channel.queue_bind(exchange="hello-world", queue="hello-consumer")


def log_to_file(log_entry: str):
    with open('./log.log', 'a+') as log_file:
        log_file.write(log_entry + '\n')
        log_file.flush()


print('Waiting for logs....')
# TODO: consume logs here
def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
channel.basic_consume(queue='aQueue',
                        auto_ack=True,
                        on_message_callback=callback)
channel.start_consuming()



