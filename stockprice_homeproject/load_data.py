from pyspark.sql import SparkSession
import pandas as pd
import os

CHUNK_SIZE = 10000

# use pyspark for large data
# Initialize Spark session
# total 10 CSV file with 1 million rows each
# Load data using spark
# read CSV file in chunks

# chunking of CSV file in spark
#


def chunk_csv(file_path, chunk_size):

    # file_path = "data/stock_prices.csv"
    schema = {
        'Date': 'string',
        'Close': 'float',
        'Volume': 'int'
    }
    spark = SparkSession.builder \
        .appName("LoadData") \
        .getOrCreate()
    spark_df = spark.read.csv(file_path, header=True, schema=schema)


# laod 10 100GB file from s3
# read CSV file in chunks
chunked_df = spark_df.limit(CHUNK_SIZE)
# write to parquet
# create add


def load_data(file_path):
    chunk_size = 10000
    chunked_df = chunk_csv(file_path, chunk_size)
    chunked_df = chunked_df.withColumn("timestamp", current_timestamp())
    chunked_df.write.parquet("data/stock_prices.parquet", mode="append")
    #
    # Check if the Delta table exists
    if DeltaTable.isDeltaTable(spark, delta_table_path):
        # If the table exists, append data
        delta_table = DeltaTable.forPath(spark, delta_table_path)
        delta_table.alias("existing").merge(
            spark_df.alias("new"),
            "existing.Date = new.Date"  # Example condition for merging
        ).whenNotMatchedInsertAll().execute()
        print("Data appended to the existing Delta table.")
    else:
        # If the table does not exist, create it
        spark_df.write.format("delta").mode("overwrite").save(delta_table_path)
        print("Delta table created and data written.")

    # Optionally, register the Delta table in the Spark catalog
    spark.sql(
        f"CREATE TABLE IF NOT EXISTS stock_prices USING DELTA LOCATION '{delta_table_path}'")

    spark_df.write.format("delta").mode(
        "overwrite").saveAsTable("stock_prices")

    # return chunked_df
    # return spark_df
    # return chunked_df
