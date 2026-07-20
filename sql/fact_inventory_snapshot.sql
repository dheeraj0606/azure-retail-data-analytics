-- File: sql/fact_inventory_snapshot.sql

INSERT INTO FactInventorySnapshot
SELECT
    GETDATE() AS SnapshotDate,
    ProductSK,
    SUM(Quantity) AS InventoryLevel
FROM staging_inventory
GROUP BY ProductSK;
