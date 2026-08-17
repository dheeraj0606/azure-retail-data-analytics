-- File: fixes/fix_partition_skew.sql

-- Repartition strategy
CREATE TABLE FactSales_Repartitioned
WITH (
    DISTRIBUTION = HASH(CustomerID)
)
AS
SELECT * FROM FactSales;
