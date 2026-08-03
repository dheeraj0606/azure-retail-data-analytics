-- File: sql/fact_order_pipeline.sql

UPDATE FactOrderPipeline
SET
    OrderShippedDate = src.ShippedDate,
    OrderDeliveredDate = src.DeliveredDate
FROM staging_orders src
WHERE FactOrderPipeline.OrderID = src.OrderID;
