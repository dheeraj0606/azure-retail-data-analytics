from tools.config_loader import load_config
from tools.file_utils import file_exists
from tools.retry_util import retry
from monitoring.metrics_logger import log_metric

def run_pipeline():
    print("Starting pipeline...")

    # Load config
    config = load_config("config/app_config.yaml")
    data_path = config.get("data_path", "data/sample_orders.csv")

    # Check file
    if not file_exists(data_path):
        raise Exception(f"File not found: {data_path}")

    print(f"Processing file: {data_path}")

    # Simulated processing
    log_metric("records_processed", 100)

    print("Pipeline completed successfully")

if __name__ == "__main__":
    retry(run_pipeline)
