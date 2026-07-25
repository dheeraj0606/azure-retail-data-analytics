# File: utils/error_handler.py

def safe_execute(func):
    try:
        return func()
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise
