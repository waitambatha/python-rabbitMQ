# RabbitMQ Publisher and Consumer

This project demonstrates a simple RabbitMQ publisher and consumer using Python and the `pika` library. The publisher script prompts the user for their name, age, gender, and hobby, and sends this information as a message to a RabbitMQ queue. The consumer script receives and displays this information.

## Prerequisites

- Python 3.x
- RabbitMQ server
- `pika` library

## Installation

1. **Install RabbitMQ**:
   Follow the instructions on the [official RabbitMQ website](https://www.rabbitmq.com/download.html) to install RabbitMQ on your machine.

2. **Install `pika` library**:
   Install the `pika` library using pip:
   ```sh
   pip install pika
Project Structure
producer.py: The publisher script that prompts the user for details and sends the message to RabbitMQ.
consumer.py: The consumer script that receives and displays the message from RabbitMQ.
Usage
Running the Consumer
First, start the RabbitMQ server if it is not already running. Then, run the consumer script:

sh
Copy code
python consumer.py
You should see a message indicating that it is waiting for messages.

Running the Publisher
Run the publisher script:

sh
Copy code
python producer.py
The script will prompt you to enter your name, age, gender, and hobby. After entering the information, the script will send the message to RabbitMQ.

Example
Start the Consumer:

sh
Copy code
python consumer.py
Output:

css
Copy code
 [*] Waiting for messages. To exit press CTRL+C
Run the Publisher:

sh
Copy code
python producer.py
Input:

mathematica
Copy code
Enter your name: John Doe
Enter your age: 30
Enter your gender: Male
Enter your hobby: Reading
Output:

css
Copy code
 [x] Sent '{"name": "John Doe", "age": "30", "gender": "Male", "hobby": "Reading"}'
Consumer Output:

yaml
Copy code
 [x] Received message:
     Name: John Doe
     Age: 30
     Gender: Male
     Hobby: Reading
Explanation
Publisher (producer.py):

Prompts the user for their name, age, gender, and hobby.
Constructs a message as a dictionary and converts it to a JSON string.
Connects to RabbitMQ, declares the test_queue, and publishes the JSON message to the queue.
Consumer (consumer.py):

Connects to RabbitMQ, declares the test_queue, and sets up a callback function to handle messages.
The callback function parses the JSON message and prints the user details.
Starts consuming messages from the queue and waits for incoming messages.
License
This project is licensed under the MIT License.

Acknowledgements
RabbitMQ for providing the messaging broker.
Pika for the Python client for RabbitMQ.
vbnet
Copy code

This `README.md` provides an overview of the project, installation instructions, usage example
