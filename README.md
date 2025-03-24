# 📊 Data Engineering Project: Real-Time Streaming Pipeline with Kafka & PySpark

## ✅ Overview
This project demonstrates an end-to-end streaming data pipeline using:
- **Kafka** for simulating real-time sales transactions.
- **PySpark Structured Streaming** for processing, aggregating, and saving results.
- **Local Parquet output** for batch analytics and future BI integration.

---

## ✅ Architecture Summary
- **Kafka (via Docker)**: Receives simulated sales transactions.
- **PySpark (Jupyter Notebook Docker)**: 
  - Connects to Kafka.
  - Consumes streaming data.
  - Aggregates sales by product category.
  - Saves results continuously as Parquet files.
- **Output**: Local Parquet files in a `/streaming_sales_output/` directory with checkpoints for fault tolerance.

---

## ✅ Folder Structure
```
project-root/
├── Kafka/
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── create-kafka-topic.sh
├── pyspark/
│   ├── spark_streaming_job.py
│   └── streaming_sales_output/ (generated)
│       ├── part-*.parquet
│       └── checkpoints/
└── Python-Sales-Simulation-Script/
    ├── sales_simulation_producer.py
    ├── generate_customer_profiles.py
    └── customer_profiles.csv
```

---

## ✅ How to Run the Pipeline

### 1️⃣ Start Kafka & Zookeeper
```bash
cd Kafka
docker-compose up -d
```

### 2️⃣ Verify Kafka topic
```bash
docker exec -it <kafka_container_id> bash
kafka-topics --list --bootstrap-server localhost:9092
```
If the `sales_transactions` topic doesn’t exist, create it:
```bash
kafka-topics --create --topic sales_transactions --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1
```

### 3️⃣ Start PySpark Jupyter Notebook
```bash
docker run -it --rm \
  -p 8888:8888 \
  -v $(pwd)/pyspark:/home/jovyan/work \
  --network data-pipeline-net \
  jupyter/pyspark-notebook
```

### 4️⃣ Run the `spark_streaming_job.py` from the notebook or as a script
- The script:
  - Connects to Kafka.
  - Aggregates sales transactions by product category in 1-minute windows.
  - Writes output continuously to Parquet.

### 5️⃣ Start the Kafka producer simulation
```bash
cd Python-Sales-Simulation-Script
python sales_simulation_producer.py
```

### 6️⃣ Check Parquet output
- Parquet files will appear in:
```
pyspark/streaming_sales_output/
```

---

## ✅ Next Steps
- Add batch job processing for `customer_profiles.csv`.
- Visualize aggregated Parquet results in a Jupyter notebook.
- Optionally deploy on Azure Blob or Databricks.

---

## ✅ Contact
Made by Youssef — feel free to connect or reach out for questions!
