from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def run():

    spark = SparkSession.builder \
        .appName("RetailSilverTransformation") \
        .getOrCreate()

    source = "abfss://bronze@stretaildev.dfs.core.windows.net/orders_delta"
    target = "abfss://silver@stretaildev.dfs.core.windows.net/orders_clean"

    df = spark.read.format("delta").load(source)

    clean_df = df \
        .withColumn("quantity", col("quantity").cast("int")) \
        .withColumn("price", col("price").cast("double"))

    clean_df.write \
        .format("delta") \
        .mode("overwrite") \
        .save(target)


if __name__ == "__main__":
    run()
