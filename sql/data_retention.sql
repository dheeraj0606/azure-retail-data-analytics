-- File: sql/data_retention.sql

DELETE FROM FactSales
WHERE CreatedDate < DATEADD(YEAR, -5, GETDATE());
