from pyspark.sql import SparkSession
from pyspark.sql.functions import sum


def run():

    spark = SparkSession.builder \
        .appName("RetailGoldAggregation") \
        .getOrCreate()

    source = "abfss://silver@stretaildev.dfs.core.windows.net/orders_clean"
    target = "abfss://gold@stretaildev.dfs.core.windows.net/product_sales"

    df = spark.read.format("delta").load(source)

    agg_df = df.groupBy("product_id") \
        .agg(sum("quantity").alias("total_units_sold"))

    agg_df.write \
        .format("delta") \
        .mode("overwrite") \
        .save(target)


if __name__ == "__main__":
    run()
