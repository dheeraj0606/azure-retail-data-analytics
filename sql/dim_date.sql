-- File: sql/dim_date.sql

CREATE TABLE dbo.DimDate (
    DateKey INT PRIMARY KEY, -- YYYYMMDD
    FullDate DATE,
    Year INT,
    Quarter INT,
    Month INT,
    MonthName VARCHAR(20),
    Day INT
);
