import mysql.connector
from auth import connection
mydb = connection()


mycursor = mydb.cursor()
sql_insert = "INSERT INTO PriceHistory (BaseCurrency, QuoteCurrency, Price) VALUES (?, ?, ?);"

# Define the values to be inserted
values = ('BTC', 'USDT', 42758.8)
mycursor.execute(sql_insert, values)
