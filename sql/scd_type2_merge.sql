-- File: sql/scd_type2_merge.sql

MERGE dbo.DimCustomer AS target
USING dbo.stg_customer AS source
ON target.CustomerID = source.CustomerID
AND target.IsCurrent = 1

WHEN MATCHED AND (
    target.Name <> source.Name OR
    target.City <> source.City
)
THEN UPDATE SET
    target.EndDate = GETDATE(),
    target.IsCurrent = 0

WHEN NOT MATCHED BY TARGET
THEN INSERT (
    CustomerID, Name, City,
    EffectiveDate, EndDate, IsCurrent
)
VALUES (
    source.CustomerID,
    source.Name,
    source.City,
    GETDATE(),
    NULL,
    1
);
