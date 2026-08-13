-- File: fixes/fix_fact_double_count.sql

-- Root cause: duplicate joins on dimension

SELECT DISTINCT
    f.SalesID,
    d.CustomerSK,
    f.Amount
FROM staging_sales f
JOIN DimCustomer d
    ON f.CustomerID = d.CustomerID
    AND d.IsCurrent = 1;
