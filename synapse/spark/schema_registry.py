from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType, TimestampType


def get_orders_schema():
    """
    Central place to define schemas for datasets.
    Helps avoid schema drift.
    """

    return StructType([
        StructField("order_id", IntegerType(), False),
        StructField("customer_id", IntegerType(), False),
        StructField("product_id", IntegerType(), False),
        StructField("quantity", IntegerType(), True),
        StructField("price", DoubleType(), True),
        StructField("order_date", TimestampType(), True)
    ])
