-- File: fixes/fix_scd_duplicate_current.sql

-- Identify duplicates
SELECT CustomerID, COUNT(*)
FROM DimCustomer
WHERE IsCurrent = 1
GROUP BY CustomerID
HAVING COUNT(*) > 1;

-- Fix logic
UPDATE DimCustomer
SET IsCurrent = 0,
    EndDate = GETDATE()
WHERE CustomerID IN (
    SELECT CustomerID
    FROM DimCustomer
    WHERE IsCurrent = 1
    GROUP BY CustomerID
    HAVING COUNT(*) > 1
)
AND EffectiveDate <> (
    SELECT MAX(EffectiveDate)
    FROM DimCustomer d2
    WHERE d2.CustomerID = DimCustomer.CustomerID
);
