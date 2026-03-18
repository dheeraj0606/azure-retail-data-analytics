def collect_metrics(df, table_name: str):
    """
    Simple dataset metrics collector.
    """

    row_count = df.count()

    metrics = {
        "table": table_name,
        "row_count": row_count
    }

    print(f"Metrics for {table_name}: {metrics}")

    return metrics
