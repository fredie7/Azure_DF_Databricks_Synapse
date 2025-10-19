### ECOMMERCE BIG DATA ANALYTICS
This project cuts across an end-to-end analytics of an Europe-based ecommerce company that seeks a robust pipeline for data migration, scalable processing and structured medallion architectural warehouse for insights gneration when needed.

#### Tools:
- Azure Data Factory
- Azure datalake
- Azure Databricks
- Azure Synapse Analytics
- Power BI

#### Data Injestion & Migration
The project starts with a dynamic data migration using data factory tools like the copy activity, foreach activity and the loopup activity. The working relationship within the pipeline are made possible using the linked-service utility which connects all end-points from the source(raw layer section of the Datalake) to the destination(bronze layer section of the datalake).
Here's a successful representation of a working pipeline after migration, configuration and loading:

<table align="center">
  <tr>
    <td align="center">
      <img src="https://github.com/fredie7/Azure_DF_Databricks_Synapse/blob/main/images/data_factory_pipeline.png?raw=true" height="300"><br>
      <sub><b></b> Data Factory Pipeline</sub>
    </td>
    <td align="center">
      <img src="https://github.com/fredie7/Azure_DF_Databricks_Synapse/blob/main/images/euro-lake-bronze.png?raw=true" height="300"><br>
      <sub><b></b> Continuous delivery of data in the bronze layer of the datalake</sub>
    </td>
  </tr>
</table>

#### Data Processing in Databricks 
The project continued with establishing a connection between databricks and azure datalake storage - This is to allow access to the data in the bronze layer og the datalake in order to facilitate data processing for the silver layer. The processing involves best practices of data quality checks for the fortification of data integrity, and data enrichment for crisp generation of insights.

#### Data Ware housing in Synapse Analytics
The data processing is followed through with an ETL process on azure synapse analytics warehouse where connections are first established between synapse and dataake using the IAM (Identtity & access management) utility.A database is created, configured, before the definition of a schema. The OPENROWSET() function formed a huge part of data migration from the silver layer of the datalake, before an external table is created to to make the data accessible to other data specialists on end users on the team.

Then Azure Synapse Analytics is connected with Power BI for bsiness insights:
