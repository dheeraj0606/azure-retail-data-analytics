CREATE TABLE IF NOT EXISTS dim_customer (
    customer_sk INT IDENTITY(1,1),  -- surrogate key
    customer_id STRING,             -- business key
    name STRING,
    email STRING,
    address STRING,

    is_current BOOLEAN,
    effective_date TIMESTAMP,
    end_date TIMESTAMP,

    PRIMARY KEY (customer_sk)
);
