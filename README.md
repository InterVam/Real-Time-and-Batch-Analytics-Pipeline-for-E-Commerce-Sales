# 📊 Batch & Streaming Data Pipeline Project

## 🚀 Overview
This project demonstrates a full end-to-end data engineering pipeline featuring both real-time streaming data ingestion and batch data processing. The pipeline simulates e-commerce transactions and customer profile data to build a scalable analytics solution.

---

## ✅ Architecture
- **Streaming Ingestion**: Kafka simulates real-time sales transactions.
- **Batch Ingestion**: Historical customer profile CSV stored locally (can be extended to S3 or Azure Blob).
- **Processing Layer**:
  - Spark Structured Streaming for real-time processing.
  - PySpark batch jobs for historical data.
- **Storage**: Simulated data lake via local directories or cloud integration.
- **Orchestration**: Airflow (optional for scheduling batch jobs).
- **Visualization**: Connect to Power BI or Looker for analytics (optional).

---

## 📂 Folder Structure
```
├── Kafka
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── create-kafka-topic.sh
│
├── Python-Sales-Simulation-Script
│   ├── generate_customer_profiles.py
│   ├── sales_simulation_producer.py
│   ├── customer_profiles.csv (generated)
│   └── customer_ids.json (generated)
│
└── pyspark
    ├── spark_batch_job.py (to be added)
    └── spark_streaming_job.py (to be added)
```

---

## 🔧 Prerequisites
- Docker & Docker Compose
- Python 3.8+
- Kafka (via Docker)
- PySpark
- pandas, faker, kafka-python (Python libraries)

---

## 🛠 Setup Instructions

### 1. Kafka Setup
```bash
cd Kafka
docker-compose up --build -d
```

### 2. Generate Historical Customer Profiles
```bash
cd Python-Sales-Simulation-Script
python generate_customer_profiles.py
```
This creates `customer_profiles.csv` and `customer_ids.json`.

### 3. Start Sales Transaction Producer
```bash
python sales_simulation_producer.py
```
This will send random transactions to Kafka.

### 4. (Optional) Consume messages for testing
```bash
docker exec -it <kafka_container_id> bash
kafka-console-consumer --topic sales_transactions --bootstrap-server kafka:9092 --from-beginning
```

---

## 🔎 Next Steps (Coming Soon)
- Add Spark streaming job to consume from Kafka and write Parquet outputs.
- Add Spark batch ETL to transform `customer_profiles.csv`.
- Connect Spark output to Snowflake or Databricks.
- Visualize aggregated metrics in Power BI.

---

## 🤝 Contributions
PRs are welcome! Feel free to fork the repo and add enhancements.

---

## 📫 Contact
Created by Youssef — [LinkedIn](https://www.linkedin.com/in/yfathi2000/) | [GitHub](https://github.com/InterVam)

