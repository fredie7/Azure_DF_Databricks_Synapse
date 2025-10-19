# CHeck for missing values in the products data
df_products.select([count(when(col(c).isNull(),c)).alias(c) for c in df_products.columns]).show()

# Check for duplicates in the products data
df_products.groupBy("product_id").agg(count("product_id").alias("count")).filter(col("count") > 1).show()

# Calculate the profit and include it among the columns
df_products = df_products.withColumn("profit", round(col("catalog_price") - col("cost_price"),2))

# Display the table
display(df_products)

# Persist table to the silver layer of the datalake
df_products.write.format("parquet")\
    .mode("append")\
        .option("path","abfss://silver@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_products")\
            .save()
