# Table overview
df_saleitems.display()

# Join the fact table(saleitems) with the channels table
df_saleitems = df_saleitems.join(df_channels, on="channel", how="left")

#Drop unwanted columns
df_saleitems = df_saleitems.drop("channel_campaigns","description","channel")

#Quality check on the fact table
df_saleitems.select([count(when(col(c).isNull(), c)).alias(c) for c in df_saleitems.columns]).show()

# Persist the table to the datalake
df_saleitems.write.format("parquet")\
    .mode("append")\
        .option("path","abfss://silver@europeanecommercestorage.dfs.core.windows.net/dataset_fashion_store_saleitems")\
            .save()

