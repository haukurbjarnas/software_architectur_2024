import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", credentials=pika.PlainCredentials("guest", "guest")
    )
)
channel = connection.channel()

channel.exchange_declare(exchange="hello-world", exchange_type="fanout")

channel.queue_declare(queue="hello-consumer-1")

channel.queue_bind(exchange="hello-world", queue="hello-consumer-1")


def callback(ch, method, properties, body):
    print(f" [x] Received from consumer 1 {body}")


channel.basic_consume(
    queue="hello-consumer-1", auto_ack=True, on_message_callback=callback
)

channel.start_consuming()
