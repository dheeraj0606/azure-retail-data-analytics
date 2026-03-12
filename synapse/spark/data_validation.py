from pyspark.sql.functions import col

def validate_orders(df):

    errors = []

    if df.filter(col("order_id").isNull()).count() > 0:
        errors.append("Null order_id detected")

    if df.filter(col("quantity") <= 0).count() > 0:
        errors.append("Invalid quantity values detected")

    if errors:
        raise Exception("Data validation failed: " + ",".join(errors))

    print("Data validation passed")
