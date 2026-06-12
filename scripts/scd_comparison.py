def scd_type1(df_target, df_source):
    return df_source  # overwrite


def scd_type2(df_target, df_source):
    # pseudo logic
    updated = df_target.join(df_source, "customer_id") \
        .where("target.address != source.address")

    # expire old + insert new
    return updated


def scd_type3(df_target, df_source):
    df = df_target.join(df_source, "customer_id", "left")

    df = df.withColumn(
        "previous_address",
        df["current_address"]
    ).withColumn(
        "current_address",
        df["address"]
    )

    return df
