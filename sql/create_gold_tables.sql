CREATE DATABASE retail_analytics;

CREATE EXTERNAL TABLE product_sales
(
    product_id INT,
    total_units_sold INT
)
WITH
(
    LOCATION = 'abfss://gold@stretaildev.dfs.core.windows.net/product_sales',
    DATA_SOURCE = retail_storage,
    FILE_FORMAT = Delta
);
