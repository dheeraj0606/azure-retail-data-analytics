def sample_data(df, fraction: float = 0.1):
    """
    Returns sampled dataframe for testing/debugging.
    """

    return df.sample(fraction)
