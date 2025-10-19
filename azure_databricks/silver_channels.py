# Include the monotinically increading id in the channels table

df_channels = df_channels.withColumn("channel_id", monotonically_increasing_id())

# Push the channels data to the silver layer of the datalake in parquet format

df_campaign.write.format("parquet")\
    .mode("append")\
        .option("path","abfss://silver@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_channels")\
            .save()
