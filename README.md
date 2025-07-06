# Real-time Data Ingestion with Delta Lake

This project demonstrates a real-time data ingestion pipeline using **PySpark**, **Delta Lake**, and **fake data generation**. It supports:

- 🔁 Periodic data generation and ingestion
- 🧪 Delta Table versioning and history tracking
- 🌍 Timezone-aware Spark processing
- 📧 Email summaries with HTML tables after each update

## Features

- Generates fake Name, Address, Email using `Faker`
- Appends to Delta Table using Delta Lake API
- Tracks Delta Table versions and timestamps
- Runs every 5 minutes (configurable)
- Sends HTML email summary after each append

## Requirements

- Python 3.10
- Apache Spark 3.x
- Delta Lake core JAR
- Java 8+
- Gmail (App Password for sending emails)

## Setup

```bash
pip install -r requirements.txt
