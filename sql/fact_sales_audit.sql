-- File: sql/fact_sales_audit.sql

ALTER TABLE FactSales
ADD LoadDate DATETIME DEFAULT GETDATE(),
    SourceSystem VARCHAR(50);
