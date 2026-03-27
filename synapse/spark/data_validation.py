def validate_non_negative(df, column_name: str):
    """
    Ensures no negative values in numeric columns.
    """

    invalid_count = df.filter(f"{column_name} < 0").count()

    if invalid_count > 0:
        raise ValueError(f"{column_name} has negative values: {invalid_count}")

    print(f"{column_name} validation passed")
