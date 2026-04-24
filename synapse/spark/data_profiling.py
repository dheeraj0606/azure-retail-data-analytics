def profile_data(df):
    print("Row count:", df.count())

    for col in df.columns:
        print(f"Column: {col}")
        print(f"Null Count: {df.filter(df[col].isNull()).count()}")
        print("-" * 30)
