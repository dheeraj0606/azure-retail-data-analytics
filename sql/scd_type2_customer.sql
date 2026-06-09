MERGE INTO dim_customer tgt
USING stg_customer src
ON tgt.customer_id = src.customer_id
   AND tgt.is_current = TRUE

WHEN MATCHED AND (
    tgt.name <> src.name OR
    tgt.address <> src.address
)
THEN UPDATE SET
    is_current = FALSE,
    end_date = CURRENT_TIMESTAMP

WHEN NOT MATCHED
THEN INSERT (
    customer_id,
    name,
    address,
    is_current,
    effective_date,
    end_date
)
VALUES (
    src.customer_id,
    src.name,
    src.address,
    TRUE,
    CURRENT_TIMESTAMP,
    NULL
);
