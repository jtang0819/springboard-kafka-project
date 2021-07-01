# springboard-kafka-project
kafka mini project
Building A Streaming Fraud Detection System With Kafka + Python


1. start kafka and zookeeper cluster
docker-compose -f docker-compose.kafka.yml up
2. run generator and detector apps.py
docker-compose up
3. check kafka legit and fraud consumers
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.legit
docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud
