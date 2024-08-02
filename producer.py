import pika
import json

def publish_message(message):
    # Connect to RabbitMQ server
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue (create if it doesn't exist)
    channel.queue_declare(queue='test_queue')

    # Publish a message to the queue
    channel.basic_publish(exchange='', routing_key='test_queue', body=message)
    print(f" [x] Sent '{message}'")

    # Close the connection
    connection.close()

if __name__ == "__main__":
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")
    hobby = input("Enter your hobby: ")

    message = {
        'name': name,
        'age': age,
        'gender': gender,
        'hobby': hobby
    }

    publish_message(json.dumps(message))
