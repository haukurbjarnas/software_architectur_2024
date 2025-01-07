#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        "localhost", credentials=pika.PlainCredentials("guest", "guest")
    )
)
channel = connection.channel()

channel.exchange_declare(exchange="hello-world", exchange_type="fanout")

channel.basic_publish(exchange="hello-world", routing_key="", body="Hello World!")

print(" [x] Sent 'Hello World!'")

connection.close()
