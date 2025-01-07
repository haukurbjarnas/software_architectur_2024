import pika
import pika.exceptions
from retry import retry


@retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
def get_connection():
    # TODO: create rabbitmq connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=pika.PlainCredentials('guest', 'guest')))
    channel = connection.channel()
    channel.queue_declare('message_queue', durable=True)
    
    def callback(ch, method, properties, body):
        print(f"Received message: {body.decode()}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='message_queue', on_message_callback=callback)
    return channel


if __name__ == '__main__':
    # TODO: consume message events and print them to console
    channel = get_connection()
    channel.start_consuming()
