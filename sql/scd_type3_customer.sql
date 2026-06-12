MERGE INTO dim_customer_type3 tgt
USING stg_customer src
ON tgt.customer_id = src.customer_id

WHEN MATCHED AND tgt.current_address <> src.address
THEN UPDATE SET
    tgt.previous_address = tgt.current_address,
    tgt.current_address = src.address,
    tgt.updated_at = CURRENT_TIMESTAMP

WHEN NOT MATCHED THEN INSERT (
    customer_id,
    name,
    current_address,
    previous_address,
    updated_at
)
VALUES (
    src.customer_id,
    src.name,
    src.address,
    NULL,
    CURRENT_TIMESTAMP
);
