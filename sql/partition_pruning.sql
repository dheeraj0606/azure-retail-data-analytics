-- File: sql/partition_pruning.sql

SELECT *
FROM FactSales
WHERE DateKey BETWEEN 20240101 AND 20240131;
