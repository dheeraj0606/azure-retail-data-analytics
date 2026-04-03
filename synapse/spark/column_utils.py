def rename_columns(df, column_mapping: dict):
    """
    Rename multiple columns using mapping dictionary.
    """

    for old_name, new_name in column_mapping.items():
        df = df.withColumnRenamed(old_name, new_name)

    return df
