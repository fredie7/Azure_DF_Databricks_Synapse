# Check table outlook
df_stock.display()

# Remove white spaces from the country column
df_stock_cleaned = df_stock.withColumn("country",trim(col("country")))

# Load to the datalake
df_stock_cleaned.write.format("parquet")\
    .mode("append")\
        .option("path","abfss://silver@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_stock")\
            .save()
