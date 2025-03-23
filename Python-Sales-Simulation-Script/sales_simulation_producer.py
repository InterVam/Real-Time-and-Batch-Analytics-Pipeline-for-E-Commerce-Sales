import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

# Load customer IDs
with open("customer_ids.json", "r") as f:
    customer_ids = [json.loads(line)["customer_id"] for line in f]

# Initialize producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

product_categories = ["Electronics", "Fashion", "Home", "Sports", "Books"]
payment_methods = ["Credit Card", "PayPal", "Apple Pay", "Google Pay"]

def generate_transaction():
    return {
        "transaction_id": random.randint(100000, 999999),
        "timestamp": datetime.utcnow().isoformat(),
        "customer_id": random.choice(customer_ids),   # <== linked customer ID
        "product_category": random.choice(product_categories),
        "amount": round(random.uniform(20.0, 1000.0), 2),
        "payment_method": random.choice(payment_methods)
    }

while True:
    transaction = generate_transaction()
    producer.send("sales_transactions", transaction)
    print(f"Sent: {transaction}")
    time.sleep(random.uniform(0.5, 2.0))
