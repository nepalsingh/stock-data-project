# Stock Price Home Project for CG Data Engineering

## Project Overview
This project is designed to provide a comprehensive solution to stocks' closing prices, dates, and stock tickers for a given date range.

The project includes the following components:
1. **Data Ingestion**: The project ingests stock data from a CSV file and stores it in a PostgreSQL database.
2. **Data Transformation**: The project transforms the data to ensure it is in the correct format for analysis.

The data consists of 100 to 200 GB CSV files.

## Data Loading and Generation
### Data Loading
- The project supports loading large CSV files into a PostgreSQL database.
- The data is partitioned and converted into Delta format for efficient querying and storage.
- The loading process includes:
  - Validating the CSV file structure.
  - Bulk inserting data into the database.
  - Creating indexes for faster querying.

### Data Generation
- Synthetic data generation is supported for testing and development purposes.
- The data generation process includes:
  - Generating random stock tickers, dates, and closing prices.
  - Ensuring the generated data adheres to realistic patterns.
  - Exporting the generated data to CSV format for ingestion.

## Future Enhancements
- Automate the data ingestion pipeline using Apache Airflow.
- Implement real-time data streaming using Kafka.
- Add support for additional data formats like JSON and Parquet.
