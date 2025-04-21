# add spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import current_timestamp
from delta.tables import DeltaTable
import os


def create_table_from_csv(file_path, delta_table_path):

    spark.session = SparkSession.builder \
        .appName("CreateTableFromCSV") \
        .getOrCreate()

    # Define the schema for the CSV file from the file in folder
    spark.sql("create table if not exists stocks_data (Date string, Close string, Volume sting, stock sting) "
              "using csv "
              "location f'abfss://{container}@{storage}.dfs.core.windows.net/data/stock_price'"
              )

    spark.sql("create database if not exists st_processes")

    spark.sql("create table if not exists st_processes.stocks_data_delta"
              " (Date timestamp, Close float, Volume int, stock string) "
              " using delta "
              "select cast(Date as data), cast(Close as float), cast(Volume as int), stock from stocks_data "
              " partition by (stock) "
              " clustered by (Date) "
              )
    # select top 100 from stocks_delta_data
    df_stockdata = spark.sql(
        "select * from st_processes.stocks_data_delta limit 100").show()
    # write to parquet
    display(df_stockdata)
