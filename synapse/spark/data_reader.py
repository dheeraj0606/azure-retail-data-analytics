def read_csv(spark, path: str, header: bool = True, infer_schema: bool = True):
    """
    Standard CSV reader utility.
    """

    return spark.read \
        .option("header", header) \
        .option("inferSchema", infer_schema) \
        .csv(path)


def read_parquet(spark, path: str):
    """
    Standard Parquet reader.
    """

    return spark.read.parquet(path)
