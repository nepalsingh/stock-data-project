# load csv files from ADLS from Azure

from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from delta.tables import DeltaTable
import os


def create_table_from_csv(file_path):
    spark = SparkSession.builder \
        .appName("CreateTableFromCSV") \
        .getOrCreate()

    # check if te table exists
    delta_table_path = "abfss://{container}@{storage}.dfs.core.windows.net/data/stock_price"
    if DeltaTable.isDeltaTable(spark, delta_table_path):
        # If the table exists, append data
        delta_table = DeltaTable.forPath(spark, delta_table_path)
        delta_table.alias("existing").merge(
            spark.read.csv(file_path, header=True).alias("new"),
            "existing.Date = new.Date"  # Example condition for merging
        ).whenNotMatchedInsertAll().execute()
        print("Data appended to the existing Delta table.")
    else:
        # If the table does not exist, create it
        spark.read.csv(file_path, header=True).write.format(
            "delta").mode("overwrite").save(delta_table_path)
        print("Delta table created and data written.")
    # Optionally, register the Delta table in the Spark catalog
    spark.sql(
        f"CREATE TABLE IF NOT EXISTS stock_prices USING DELTA LOCATION '{delta_table_path}'")

# read from all csv files in the folder


def read_csv_files_from_folder(folder_path):
    spark = SparkSession.builder \
        .appName("ReadCSVFiles") \
        .getOrCreate()

  # call create_table_from_csv for each file in the folder
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            create_table_from_csv(file_path)
