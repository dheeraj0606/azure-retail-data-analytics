from pyspark.sql.functions import col, current_timestamp

def scd_type2_merge(spark):
    src = spark.table("stg_customer")
    tgt = spark.table("dim_customer")

    join_condition = "tgt.customer_id = src.customer_id AND tgt.is_current = true"

    (
        tgt.alias("tgt")
        .merge(
            src.alias("src"),
            join_condition
        )
        .whenMatchedUpdate(
            condition="""
                tgt.name <> src.name OR
                tgt.email <> src.email OR
                tgt.address <> src.address
            """,
            set={
                "is_current": "false",
                "end_date": "current_timestamp()"
            }
        )
        .whenNotMatchedInsert(
            values={
                "customer_id": "src.customer_id",
                "name": "src.name",
                "email": "src.email",
                "address": "src.address",
                "is_current": "true",
                "effective_date": "current_timestamp()",
                "end_date": "null"
            }
        )
        .execute()
    )
