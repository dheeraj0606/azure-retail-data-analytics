# File: pipelines/schema_evolution.py

def align_schema(df, target_columns):
    for col in target_columns:
        if col not in df.columns:
            df = df.withColumn(col, None)
    return df
