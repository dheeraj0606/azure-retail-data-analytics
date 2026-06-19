-- File: sql/optimize_tables.sql

OPTIMIZE dim_customer
ZORDER BY (CustomerID);

VACUUM dim_customer RETAIN 168 HOURS;
