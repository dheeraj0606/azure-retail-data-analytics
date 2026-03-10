from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailBronze").getOrCreate()

df = spark.read.option("header",True).csv("/bronze/orders")

df.show()
