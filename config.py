# config.py

EMAIL_SENDER = "gmail.com"          # Gmail (use App Password below)
EMAIL_PASSWORD = "####### #### ###"        # App Password only
EMAIL_RECEIVER = "gmail.com"  # Receiver email

DELTA_PATH = "file:///C:/Users/HP/real_time_data_ingestion/delta/people_data"
INTERVAL_SECONDS = 300     # 5 minutes
NUM_ROWS = 5               # Number of rows per batch
TIMEZONE = "Asia/Kolkata"  # Spark timezone
