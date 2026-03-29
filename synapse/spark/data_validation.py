def validate_not_null(df, column_name: str):
    """
    Ensures column does not contain null values.
    """

    null_count = df.filter(f"{column_name} IS NULL").count()

    if null_count > 0:
        raise ValueError(f"{column_name} contains null values: {null_count}")

    print(f"{column_name} null check passed")
