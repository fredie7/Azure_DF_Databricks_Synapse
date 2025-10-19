-- CREATE VIEW FOR THE FACT TABLE (SALEITEMS)
CREATE VIEW gold.fact_saleitems
AS
SELECT
*
FROM
    OPENROWSET(
        BULK 'https://europeanecommercestorage.blob.core.windows.net/silver/dataset_fashion_store_saleitems/',
        FORMAT = 'PARQUET'
    ) AS fact_saleitems

-- CREATE VIEW FOR THE DIMENSION TABLE (SALES)
CREATE VIEW gold.dim_sales
AS
SELECT
*
FROM
    OPENROWSET(
        BULK 'https://europeanecommercestorage.blob.core.windows.net/silver/dataset_fashion_store_sales/',
        FORMAT = 'PARQUET'
    ) AS dim_sales

-- CREATE VIEW FOR THE DIMENSION TABLE (PRODUCTS)
CREATE VIEW gold.dim_products
AS
SELECT
*
FROM
    OPENROWSET(
        BULK 'https://europeanecommercestorage.blob.core.windows.net/silver/dataset_fashion_store_products/',
        FORMAT = 'PARQUET'
    ) AS dim_products

-- CREATE VIEW FOR THE DIMENSION TABLE (CUSTOMERS)
CREATE VIEW gold.dim_customers
AS
SELECT
*
FROM
    OPENROWSET(
        BULK 'https://europeanecommercestorage.blob.core.windows.net/silver/dataset_fashion_store_customers/',
        FORMAT = 'PARQUET'
    ) AS dim_customers

-- CREATE VIEW FOR THE DIMENSION TABLE (CAMPAIGNS)
CREATE VIEW gold.dim_campaigns
AS
SELECT
*
FROM
    OPENROWSET(
        BULK 'https://europeanecommercestorage.blob.core.windows.net/silver/dataset_fashion_store_campaigns/',
        FORMAT = 'PARQUET'
    ) AS dim_campaigns

-- CREATE VIEW FOR THE DIMENSION TABLE (CHANNELS)
CREATE VIEW gold.dim_channels
AS
SELECT
*
FROM
    OPENROWSET(
        BULK 'https://europeanecommercestorage.blob.core.windows.net/silver/dataset_fashion_store_channels/',
        FORMAT = 'PARQUET'
    ) AS dim_channels

-- CREATE VIEW FOR THE DIMENSION TABLE (STOCK)
CREATE VIEW gold.dim_stock
AS
SELECT
*
FROM
    OPENROWSET(
        BULK 'https://europeanecommercestorage.blob.core.windows.net/silver/dataset_fashion_store_stock/',
        FORMAT = 'PARQUET'
    ) AS dim_stock

