-- File: sql/fact_sales.sql

CREATE TABLE dbo.FactSales (
    SalesSK BIGINT IDENTITY(1,1) PRIMARY KEY,

    DateKey INT,
    CustomerSK INT,
    ProductSK INT,
    StoreSK INT,

    Quantity INT,
    UnitPrice DECIMAL(10,2),
    TotalAmount DECIMAL(12,2),

    CreatedDate DATETIME DEFAULT GETDATE()
)
WITH (
    DISTRIBUTION = HASH(CustomerSK),
    CLUSTERED COLUMNSTORE INDEX
);
