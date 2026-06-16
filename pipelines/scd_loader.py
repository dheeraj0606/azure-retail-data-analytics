# File: pipelines/scd_loader.py

from pyspark.sql.functions import col, current_date, lit

def apply_scd_type2(source_df, target_df):
    join_cond = "source.CustomerID = target.CustomerID AND target.IsCurrent = 1"

    updates = source_df.alias("source").join(
        target_df.alias("target"),
        join_cond
    ).where(
        (col("source.Name") != col("target.Name")) |
        (col("source.City") != col("target.City"))
    )

    expired = updates.selectExpr(
        "target.CustomerID",
        "target.Name",
        "target.City",
        "target.EffectiveDate",
        "current_date() as EndDate",
        "0 as IsCurrent"
    )

    new_rows = source_df.selectExpr(
        "CustomerID",
        "Name",
        "City",
        "current_date() as EffectiveDate",
        "NULL as EndDate",
        "1 as IsCurrent"
    )

    return expired.union(new_rows)
