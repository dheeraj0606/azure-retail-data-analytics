MERGE INTO dim_customer tgt
USING stg_customer src
ON tgt.customer_id = src.customer_id

WHEN MATCHED THEN UPDATE SET
    tgt.name = src.name,
    tgt.email = src.email,
    tgt.address = src.address

WHEN NOT MATCHED THEN INSERT (
    customer_id, name, email, address
)
VALUES (
    src.customer_id, src.name, src.email, src.address
);
