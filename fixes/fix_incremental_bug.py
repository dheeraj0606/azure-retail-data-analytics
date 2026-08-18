# File: fixes/fix_incremental_bug.py

from pyspark.sql.functions import col

def correct_incremental(df, last_load):
    return df.filter(col("CreatedDate") >= last_load)
