### ECOMMERCE BIG DATA ANALYTICS
This project cuts across an end-to-end analytics of an Europe-based ecommerce company that seeks a robust pipeline for data migration, scalable processing and structured medallion architectural warehouse for insights gneration when needed.

### Tools:
- Azure Data Factory
- Azure datalake
- Azure Databricks
- Azure Synapse Analytics
- Power BI

The project starts with a dynamic data migration using data factory tools like the copy activity, foreach activity and the loopup activity. The working relationship within the pipeline are made possible using the linked-service utility which connects all end-points from the source(raw layer section of the Datalake) to the destination(bronze layer section of the datalake).
Here's a successful representation of a working pipeline after migration, configuration and loading:

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/fredie7/Azure_DF_Databricks_Synapse/blob/main/images/data_factory_pipeline.png?raw=true" height="300"><br>
      <sub><b>Fig 2.</b> Tool Calls</sub>
    </td>
    <td align="center">
      <img src="https://github.com/fredie7/Azure_DF_Databricks_Synapse/blob/main/images/euro-lake-bronze.png?raw=true" height="300"><br>
      <sub><b>Fig 3.</b> Tools Interaction</sub>
    </td>
  </tr>
</table>
