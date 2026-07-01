# File: quality/data_checks.py

def validate_not_null(df, column):
    return df.filter(f"{column} IS NULL").count() == 0

def validate_positive(df, column):
    return df.filter(f"{column} < 0").count() == 0
