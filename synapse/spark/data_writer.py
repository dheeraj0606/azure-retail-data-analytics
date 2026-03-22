
def write_delta(df, path: str, mode: str = "overwrite"):
    """
    Standardized Delta write function.
    """

    df.write \
        .format("delta") \
        .mode(mode) \
        .save(path)


def write_parquet(df, path: str, mode: str = "overwrite"):
    """
    Standardized Parquet write function.
    """

    df.write \
        .format("parquet") \
        .mode(mode) \
        .save(path)
