import pandas as pd

def validate_data(df: pd.DataFrame):
    errors = []

    if df.empty:
        errors.append("Dataset is empty")

    if df.isnull().sum().sum() > 0:
        errors.append("Null values detected")

    if "amount" in df.columns and (df["amount"] < 0).any():
        errors.append("Negative amounts found")

    return errors


if __name__ == "__main__":
    df = pd.read_csv("data/sample.csv")
    issues = validate_data(df)

    if issues:
        print("Data Quality Issues:")
        for i in issues:
            print("-", i)
    else:
        print("Data validation passed")
