import time
import pytz
import pandas as pd
from faker import Faker
from datetime import datetime
from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip
from delta.tables import DeltaTable
from config import DELTA_PATH, INTERVAL_SECONDS, NUM_ROWS, TIMEZONE
from email_utils import send_email

fake = Faker()
timezone = pytz.timezone(TIMEZONE)

from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder.appName("RealTimeIngestion") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .config("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.AzureLogStore") \
    .config("spark.hadoop.hadoop.native.lib", "false")

spark = configure_spark_with_delta_pip(builder).getOrCreate()
spark.conf.set("spark.sql.session.timeZone", "Asia/Kolkata")




def generate_fake_data(n):
    data = [{"name": fake.name(), "address": fake.address(), "email": fake.email(), "ingest_time": datetime.now(timezone)} for _ in range(n)]
    return spark.createDataFrame(pd.DataFrame(data))

def append_to_delta(df):
    df.write.format("delta").mode("append").save(DELTA_PATH)

def get_latest_data():
    delta_table = DeltaTable.forPath(spark, DELTA_PATH)
    df = delta_table.toDF()
    latest_time = df.agg({"ingest_time": "max"}).collect()[0][0]
    return df.filter(df["ingest_time"] == latest_time).toPandas()

def run_pipeline():
    while True:
        df = generate_fake_data(NUM_ROWS)
        append_to_delta(df)
        latest = get_latest_data()

        html_summary = latest.to_html(index=False)
        send_email("Delta Table Update Summary", html_summary)
        
        print("Appended and emailed:\n", latest)
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    run_pipeline()
