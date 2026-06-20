-- File: sql/dim_product.sql

CREATE TABLE dbo.DimProduct (
    ProductSK INT IDENTITY(1,1) PRIMARY KEY,
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),

    EffectiveDate DATE,
    EndDate DATE,
    IsCurrent BIT
);
