import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(" [x] Received message:")
    print(f"     Name: {message['name']}")
    print(f"     Age: {message['age']}")
    print(f"     Gender: {message['gender']}")
    print(f"     Hobby: {message['hobby']}")

def consume_messages():
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue (create if it doesn't exist)
    channel.queue_declare(queue='test_queue')

    # Set up subscription on the queue
    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages()
