# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "c03b6217-c936-4dd6-a55b-61f8364fc766",
# META       "default_lakehouse_name": "Lake",
# META       "default_lakehouse_workspace_id": "bad0ef94-c17d-429b-80d8-ffe0cee9b0a7",
# META       "known_lakehouses": [
# META         {
# META           "id": "c03b6217-c936-4dd6-a55b-61f8364fc766"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

flights_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("Files/source-files/flights.csv")

display(flights_df)


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
