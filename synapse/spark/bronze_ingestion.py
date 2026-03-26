from time_utils import current_timestamp
from metrics_collector import collect_metrics
from logger import get_logger

logger = get_logger("bronze_ingestion")

logger.info(f"Bronze ingestion started at {current_timestamp()}")

# after dataframe load
collect_metrics(df, "bronze_orders")

logger.info(f"Bronze ingestion completed at {current_timestamp()}")
