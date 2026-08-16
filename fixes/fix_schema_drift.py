# File: fixes/fix_schema_drift.py

def enforce_schema(df, expected_cols):
    for col in expected_cols:
        if col not in df.columns:
            df = df.withColumn(col, None)
    return df.select(expected_cols)
