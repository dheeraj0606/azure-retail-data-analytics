import time

def log_metric(name, value):
    timestamp = int(time.time())
    print(f"{timestamp} | {name} = {value}")
