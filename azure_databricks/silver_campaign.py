# Modify the discount_rate of the camaign data into a unified fashion

df_campaign = df_campaign.withColumn("discount_value",concat(
    regexp_replace(
        regexp_replace(col("discount_value"),"%",""), 
        r"\.0+$",""
    )
    , lit("%")))

# Push the transformed campaign data to the silver layer of the datalake in parquet format

df_campaign.write.format("parquet")\
    .mode("append")\
        .option("path","abfss://silver@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_campaigns")\
            .save()
