# Data qyality check

# Check for NULL values
df_sales.select([count(when(col(c).isNull(), c)).alias(c) for c in df_sales.columns]).show()

#Check for duplicates
df_sales.groupBy("sale_id").agg(count("*").alias("count")).filter(col("count") > 1).show()

# Find unique discount values
df_sales.select("discounted").distinct().show()

# Refine the discounted column
df_sales = df_sales.withColumn("discounted_flag", when(col("discounted") == 1, True).otherwise(False))

# Load sales data in the silver layer
df_sales.write.format("parquet")\
    .mode("append")\
        .option("path","abfss://silver@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_sales")\
            .save()
