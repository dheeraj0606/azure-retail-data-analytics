# File: fixes/fix_null_sk.py

def fix_null_sk(df):
    return df.fillna({"CustomerSK": -1, "ProductSK": -1})
