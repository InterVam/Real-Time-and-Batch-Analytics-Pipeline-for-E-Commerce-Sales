import pandas as pd
import random
from faker import Faker

# Initialize Faker for realistic random data
fake = Faker()

# Define how many profiles you want to generate
NUM_CUSTOMERS = 1000

# Possible customer categories
customer_segments = ["Regular", "Premium", "VIP"]

data = []

for _ in range(NUM_CUSTOMERS):
    profile = {
        "customer_id": fake.random_int(min=1000, max=9999),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "signup_date": fake.date_between(start_date="-3y", end_date="today"),
        "country": fake.country(),
        "customer_segment": random.choice(customer_segments),
        "lifetime_value": round(random.uniform(100, 10000), 2)
    }
    data.append(profile)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("customer_profiles.csv", index=False)

print("✅ Generated customer_profiles.csv with", NUM_CUSTOMERS, "records.")

# Save customer IDs in a separate file for later use by the transactions producer
df[['customer_id']].to_json("customer_ids.json", orient="records", lines=True)

print("✅ Saved customer_ids.json for transaction simulation.")

