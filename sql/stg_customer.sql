CREATE OR REPLACE TABLE stg_customer AS
SELECT
    customer_id,
    name,
    email,
    address,
    CURRENT_TIMESTAMP AS load_time
FROM raw.customer_source;
