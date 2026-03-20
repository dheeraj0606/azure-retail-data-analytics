import time


def retry(func, retries=3, delay=5):
    """
    Retry wrapper for unreliable operations like file reads or writes.
    """

    for attempt in range(1, retries + 1):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt} failed: {str(e)}")

            if attempt == retries:
                raise

            time.sleep(delay)
