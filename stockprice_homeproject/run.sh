python create-data.py --stock_name AMZN
python create-data.py --stock_name AXP
python create-data.py --stock_name AMGN
python create-data.py --stock_name AAPL
python create-data.py --stock_name BA
python create-data.py --stock_name CAT
python create-data.py --stock_name CSCO
python create-data.py --stock_name CVX
python create-data.py --stock_name GS
python create-data.py --stock_name HD
python create-data.py --stock_name HON
python create-data.py --stock_name IBM
python create-data.py --stock_name JNJ
python create-data.py --stock_name KO
python create-data.py --stock_name JPM
python create-data.py --stock_name MCD
python create-data.py --stock_name MRK
python create-data.py --stock_name MSFT
python create-data.py --stock_name NKE
python create-data.py --stock_name PG
python create-data.py --stock_name SHW
python create-data.py --stock_name TRV
python create-data.py --stock_name UNH
python create-data.py --stock_name CRM
python create-data.py --stock_name NVDA
python create-data.py --stock_name VZ
python create-data.py --stock_name V
python create-data.py --stock_name WMT
python create-data.py --stock_name DIS

echo "Date,Close,Volume,Stock" > all_stocks.csv

for file in *.csv
do
    # Skip the first line of each file
    tail -n +2 "$file" >> all_stocks.csv
done