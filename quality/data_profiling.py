# File: quality/data_profiling.py

def profile(df):
    return {
        "row_count": df.count(),
        "columns": len(df.columns)
    }
