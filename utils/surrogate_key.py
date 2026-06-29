# File: utils/surrogate_key.py

from pyspark.sql.functions import monotonically_increasing_id

def add_surrogate_key(df, column_name="SK"):
    return df.withColumn(column_name, monotonically_increasing_id())
