# File: pipelines/deduplication.py

def deduplicate(df, keys):
    return df.dropDuplicates(keys)
