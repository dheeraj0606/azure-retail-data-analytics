SELECT
    customer_id,
    name,
    email,
    address,
    MD5(CONCAT(name, email, address)) AS hash_diff
FROM stg_customer;
