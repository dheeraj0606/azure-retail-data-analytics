-- File: sql/dim_customer_partitioned.sql

CREATE TABLE dbo.DimCustomer (
    CustomerSK INT IDENTITY(1,1),
    CustomerID INT NOT NULL,
    Name VARCHAR(100),
    City VARCHAR(50),

    EffectiveDate DATE NOT NULL,
    EndDate DATE,
    IsCurrent BIT NOT NULL,

    CreatedDate DATETIME DEFAULT GETDATE()
)
WITH (
    DISTRIBUTION = HASH(CustomerID),
    CLUSTERED COLUMNSTORE INDEX
);
