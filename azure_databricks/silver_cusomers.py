# Check for null values in the customers data
df_customers.select([count(when(col(c).isNull(), c)).alias(c)for c in df_customers.columns]).show()

# Check for duplicate customer_id
df_customers.groupBy("customer_id").agg(count("*").alias("count")).filter(col("count") > 1).show()

# Extract the signup year
df_customers = df_customers.withColumn("signup_year", year(col("signup_date")))

# Categorize the age range
# First, find the distinct age range

df_customers.select("age_range").distinct().show()

# Show customers table
df_customers.display()

# Append customers data to the datalake
df_customers.write.format("parquet")\
    .mode("append")\
        .option("path","abfss://silver@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_customers")\
            .save()
