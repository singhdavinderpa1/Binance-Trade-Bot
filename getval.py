# Import libraries 
import json 
import requests 
import time
from auth import connection
import mysql.connector


mydb = connection()

trade_pairs = ['BTCUSDT',
               'SOLEUR', 
               'MATICEUR', 
               'ETHEUR', 
               'BNBEUR', 
               "BTCEUR", 
               'AVAXEUR',
               'ADAEUR']
# defining key/request url 
key = "https://api.binance.com/api/v3/ticker/price?symbol="

mapping = {"BTCUSDT": 'BTC',
           "SOLEUR": 'SOL',
           'MATICEUR': "MATIC",
           "ETHEUR": 'ETH',
           'BNBEUR':'BNB',
           'BTCEUR': "BTCEUR",
           'TIAEUR': "TIA",
           'AVAXEUR': 'AVAX',
           'ADAEUR': 'ADA'}

statement = ""
# requesting data from url 
for pair in trade_pairs:
    # print(time.time())
    data = requests.get(f"{key}{pair}") 
    # time.sleep(10)
    # print(data)
    data = data.json() 
    # time.sleep(10)
    print(f"{data['symbol']} price is {data['price']:.7}", end = " ") 
    statement = statement + f"{data['symbol']} price is {data['price']:.7}"

    mycursor = mydb.cursor()
    sql_insert = "INSERT INTO Binance.PriceHistory (Currency, Price) VALUES (%s, %s);" 
    values = (mapping[pair], data['price'])
    values
    mycursor.execute(sql_insert, values)
    mydb.commit()
print()
