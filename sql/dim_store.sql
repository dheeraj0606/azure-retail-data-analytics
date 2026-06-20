-- File: sql/dim_store.sql

CREATE TABLE dbo.DimStore (
    StoreSK INT IDENTITY(1,1) PRIMARY KEY,
    StoreID INT,
    StoreName VARCHAR(100),
    City VARCHAR(50),
    Country VARCHAR(50)
);
