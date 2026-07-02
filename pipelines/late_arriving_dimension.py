# File: pipelines/late_arriving_dimension.py

def handle_late_arriving(df, dim_df):
    return df.join(dim_df, "CustomerID", "left") \
             .fillna({"CustomerSK": -1})
