from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest'
)

for message in consumer:
    print(f"Consumed message: {message.value.decode('utf-8')}")
