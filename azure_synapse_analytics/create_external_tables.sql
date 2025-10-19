-- CREATE MASTER KEY ENCRYPTION BY PASSWORD ='password_created'

-- CREATE CREDENTIAL - Inform that managed identity had been created earlier
CREATE DATABASE SCOPED CREDENTIAL fredie_credential
WITH 
    IDENTITY = 'Managed Identity'

-- CREATE ETERNAL DATA SOURCES (SILVER LAYER)
CREATE EXTERNAL DATA SOURCE source_silver
WITH
(
    LOCATION = 'https://europeanecommercestorage.blob.core.windows.net/silver',
    CREDENTIAL = fredie_credential
)

-- CREATE ETERNAL DATA SOURCES (GOLD LAYER)
CREATE EXTERNAL DATA SOURCE source_gold
WITH
(
    LOCATION = 'https://europeanecommercestorage.blob.core.windows.net/gold',
    CREDENTIAL = fredie_credential
)

-- CREATE EXTERNAL FILE FORMAT
CREATE EXTERNAL FILE FORMAT parquet_format
WITH
(
    FORMAT_TYPE = PARQUET,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
)

-- CREATE EXTERNAL FACT TABLE
CREATE EXTERNAL TABLE gold.ext_fact_saleitems
WITH
(
    LOCATION = 'ext_fact_saleitems',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * from gold.fact_saleitems

-- CREATE EXTERNAL DIMENSION CUSTOMERS TABLE
CREATE EXTERNAL TABLE gold.ext_dim_customers
WITH
(
    LOCATION = 'ext_dim_customers',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * from gold.dim_customers

-- CREATE EXTERNAL DIMENSION PRODUCTS TABLE
CREATE EXTERNAL TABLE gold.ext_dim_products
WITH
(
    LOCATION = 'ext_dim_products',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * from gold.dim_products

-- CREATE EXTERNAL DIMENSION SALES TABLE
CREATE EXTERNAL TABLE gold.ext_dim_sales
WITH
(
    LOCATION = 'ext_dim_sales',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * from gold.dim_sales

-- CREATE EXTERNAL DIMENSION CAMPAIGNS TABLE
CREATE EXTERNAL TABLE gold.ext_dim_campaigns
WITH
(
    LOCATION = 'ext_dim_campaigns',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * from gold.dim_campaigns

-- CREATE EXTERNAL DIMENSION CHANNELS TABLE
CREATE EXTERNAL TABLE gold.ext_dim_channels
WITH
(
    LOCATION = 'ext_dim_channels',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * from gold.dim_channels

-- CREATE EXTERNAL DIMENSION STOCK TABLE
CREATE EXTERNAL TABLE gold.ext_dim_stock
WITH
(
    LOCATION = 'ext_dim_stock',
    DATA_SOURCE = source_gold,
    FILE_FORMAT = parquet_format
)
AS
SELECT * from gold.dim_stock

-- SELECT * from gold.ext_dim_stock
