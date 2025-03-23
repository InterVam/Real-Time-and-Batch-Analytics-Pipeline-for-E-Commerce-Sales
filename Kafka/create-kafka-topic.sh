#!/bin/bash

echo "Creating Kafka topic: sales_transactions..."
kafka-topics --create \
  --topic sales_transactions \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1 \
  --if-not-exists

echo "Topic creation completed."
