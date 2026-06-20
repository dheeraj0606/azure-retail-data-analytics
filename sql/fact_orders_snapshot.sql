-- File: sql/fact_orders_snapshot.sql

CREATE TABLE dbo.FactOrdersSnapshot (
    SnapshotDate DATE,
    OrderID INT,
    CustomerSK INT,

    OrderStatus VARCHAR(50),
    TotalAmount DECIMAL(12,2),

    PRIMARY KEY (SnapshotDate, OrderID)
);
