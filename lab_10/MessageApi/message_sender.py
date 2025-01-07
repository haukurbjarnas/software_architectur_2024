import pika
import pika.credentials
from retry import retry


class MessageSender:
    def __init__(self) -> None:
        # TODO: initate connection
        self.queue_name = 'message_queue'
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=pika.PlainCredentials('guest', 'guest')))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)

    def send_message(self, message):
        # TODO: send message via rabbitmq
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message,
            properties=pika.BasicProperties(delivery_mode=2)
        )

    @retry(pika.exceptions.AMQPConnectionError, delay=5, jitter=(1, 3))
    def __get_connection(self):
        # TODO: create rabbitmq connection
        return pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost', 
            credentials=pika.PlainCredentials('guest', 'guest')
            )
        )
