# File: utils/secrets.py

import os

def get_secret(key):
    return os.getenv(key)
