# Establish connection between databricks and datalake
#spark.conf.set("fs.azure.account.auth.type.europeanecommercestorage.dfs.core.windows.net", "OAuth")
#spark.conf.set("fs.azure.account.oauth.provider.type.europeanecommercestorage.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
#spark.conf.set("fs.azure.account.oauth2.client.id.europeanecommercestorage.dfs.core.windows.net", "baec1c51-44fe-42c7-bf73-4575e56bae42")
#spark.conf.set("fs.azure.account.oauth2.client.secret.europeanecommercestorage.dfs.core.windows.net", "{secret}")
#spark.conf.set("fs.azure.account.oauth2.client.endpoint.europeanecommercestorage.dfs.core.windows.net", "https://login.microsoftonline.com/4f76d3ed-73a3-4ae8-9e8f-8d39080d6434/oauth2/token")

# Read store channels data
df_channels = spark.read.format("csv")\
    .option("header", True)\
        .option("inferSchema", True)\
            .load("abfss://bronze@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_channels")

# Read customers data
df_customers = spark.read.format("csv")\
    .option("header", True)\
        .option("inferSchema", True)\
            .load("abfss://bronze@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_customers")

# Read products data
df_products = spark.read.format("csv")\
    .option("header", True)\
        .option("inferSchema", True)\
            .load("abfss://bronze@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_products")

# Read sales data
df_sales = spark.read.format("csv")\
    .option("header", True)\
        .option("inferSchema", True)\
            .load("abfss://bronze@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_sales")

# Read salesitems data
df_saleitems = spark.read.format("csv")\
    .option("header", True)\
        .option("inferSchema", True)\
            .load("abfss://bronze@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_salesitems")

# Read stock data
df_stock = spark.read.format("csv")\
    .option("header", True)\
        .option("inferSchema", True)\
            .load("abfss://bronze@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_stock")
