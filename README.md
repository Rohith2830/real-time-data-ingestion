# 📊 Real-Time Data Ingestion Pipeline using PySpark & Delta Lake

## 🚀 Project Overview

This project implements a **real-time data ingestion pipeline** that generates fake data (Name, Email, Address), appends it to a **Delta Lake table**, tracks **versioning**, handles **time zones**, and sends **email notifications** with HTML summaries of the new data.

> ✅ Developed as part of an internship at **Cebel Technologies**.

---

## 💠 Features

* ✅ Fake data generation using `Faker`
* ✅ Append data to **Delta Lake**
* ✅ Maintain **version history** of the table
* ✅ Retrieve **latest snapshot** using timestamp logic
* ✅ Timezone-aware (`Asia/Kolkata`)
* ✅ Send **HTML email** summaries after each run
* ✅ **Scheduled every 5 minutes** using Task Scheduler
* ✅ Full automation via `.bat` script

---

## 📁 Folder Structure

```
real_time_data_ingestion/
│
├── main.py                 # Main pipeline script
├── config.py               # Configurations (paths, email, interval)
├── email_utils.py          # Email sending helper
├── requirements.txt        # Python dependencies
├── README.md               # Documentation
└── scheduler.bat           # Batch file to schedule pipeline
```

---

## 🥪 Sample Email Output

![image](https://github.com/user-attachments/assets/10c90c94-4706-4c7c-abbe-44206649291b)

---

## 🕒 Scheduling the Pipeline

**Step 1:** Use the `scheduler.bat` file:

```bat
cd C:\Users\HP\real_time_data_ingestion
spark-submit --packages io.delta:delta-core_2.12:2.3.0 main.py
```

**Step 2:** Add a **Task Scheduler Job** in Windows to run this file every 5 minutes.

---

## 📦 Dependencies

* Python 3.10+
* PySpark
* Delta Lake
* Faker
* `smtplib` for email

Install using:

```bash
pip install -r requirements.txt
```

---

## 📌 Use Cases

* Streaming ingestion simulation
* Testing Delta Lake integration
* Scheduled data pipelines
* Email automation from Spark jobs

---

## 👨‍💼 Author

**Rohith Vadlamudi**
📧 [rohithvadlamudi.28@gmail.com](mailto:rohithvadlamudi.28@gmail.com)
