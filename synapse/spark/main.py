from spark_session import get_spark_session
from bronze_ingestion import run_bronze


def main():
    spark = get_spark_session()

    print("Starting pipeline...")
    run_bronze(spark)

    print("Pipeline completed")


if __name__ == "__main__":
    main()
