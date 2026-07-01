# File: pipelines/incremental_fact_loader.py

from pyspark.sql.functions import col

def filter_incremental(df, last_load_date):
    return df.filter(col("CreatedDate") > last_load_date)
