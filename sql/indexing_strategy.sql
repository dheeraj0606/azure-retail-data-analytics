-- File: sql/indexing_strategy.sql

CREATE NONCLUSTERED INDEX idx_customer
ON DimCustomer(CustomerID)
WHERE IsCurrent = 1;
