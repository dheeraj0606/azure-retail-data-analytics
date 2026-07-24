# File: utils/retry.py

import time

def retry(func, retries=3, delay=5):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt == retries - 1:
                raise
            time.sleep(delay)
