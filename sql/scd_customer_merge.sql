MERGE INTO dim_customer tgt
USING stg_customer src
ON tgt.customer_id = src.customer_id
   AND tgt.is_current = TRUE

-- Step 1: If data changed → expire old record
WHEN MATCHED AND (
    tgt.name <> src.name OR
    tgt.email <> src.email OR
    tgt.address <> src.address
)
THEN UPDATE SET
    tgt.is_current = FALSE,
    tgt.end_date = CURRENT_TIMESTAMP

-- Step 2: Insert new record
WHEN NOT MATCHED
THEN INSERT (
    customer_id,
    name,
    email,
    address,
    is_current,
    effective_date,
    end_date
)
VALUES (
    src.customer_id,
    src.name,
    src.email,
    src.address,
    TRUE,
    CURRENT_TIMESTAMP,
    NULL
);
