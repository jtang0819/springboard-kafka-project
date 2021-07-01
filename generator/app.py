import os
from time import sleep
from transactions import create_random_transaction
import json
from kafka import KafkaProducer

KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)

if __name__ == "__main__":
    producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER_URL)
    while True:
        transaction: dict = create_random_transaction()
        message: str = json.dumps(transaction)
        producer.send("queuing.transactions", value=message.encode())
        sleep(1)

