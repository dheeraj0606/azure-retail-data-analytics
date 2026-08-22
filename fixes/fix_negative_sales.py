# File: fixes/fix_negative_sales.py

def filter_invalid_sales(df):
    return df.filter("Amount > = 0")
