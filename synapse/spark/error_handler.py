def handle_errors(func):
    """
    Decorator to standardize error handling in Spark jobs.
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred: {str(e)}")
            raise

    return wrapper
