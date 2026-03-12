from pyspark.sql import SparkSession

def run():

    spark = SparkSession.builder \
        .appName("RetailBronzeIngestion") \
        .getOrCreate()

    source_path = "abfss://bronze@stretaildev.dfs.core.windows.net/orders/orders.csv"
    target_path = "abfss://bronze@stretaildev.dfs.core.windows.net/orders_delta"

    df = spark.read \
        .option("header", True) \
        .csv(source_path)

    print("Raw dataset preview")
    df.show()

    df.write \
        .format("delta") \
        .mode("overwrite") \
        .save(target_path)


if __name__ == "__main__":
    run()
