# File: pipelines/fact_sales_loader.py

from pyspark.sql.functions import col

def load_fact_sales(sales_df, dim_customer, dim_product, dim_store):

    fact_df = sales_df \
        .join(dim_customer, "CustomerID") \
        .join(dim_product, "ProductID") \
        .join(dim_store, "StoreID") \
        .select(
            col("DateKey"),
            col("CustomerSK"),
            col("ProductSK"),
            col("StoreSK"),
            col("Quantity"),
            col("UnitPrice"),
            (col("Quantity") * col("UnitPrice")).alias("TotalAmount")
        )

    return fact_df
