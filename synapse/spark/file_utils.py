from pyspark.sql import SparkSession


def list_files(spark: SparkSession, path: str):
    """
    Utility to list files in ADLS path.
    Useful for debugging ingestion jobs.
    """

    files = spark._jvm.org.apache.hadoop.fs.FileSystem.get(
        spark._jsc.hadoopConfiguration()
    ).listStatus(
        spark._jvm.org.apache.hadoop.fs.Path(path)
    )

    return [file.getPath().toString() for file in files]
