# File: fixes/fix_timezone.py

from pyspark.sql.functions import to_utc_timestamp

def normalize_timezone(df):
    return df.withColumn("CreatedDate", to_utc_timestamp("CreatedDate", "UTC"))
