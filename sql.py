import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Nannuu95",
  database = 'Binance'
)


mycursor = mydb.cursor()
sql_insert = "INSERT INTO PriceHistory (BaseCurrency, QuoteCurrency, Price) VALUES (?, ?, ?);"

# Define the values to be inserted
values = ('BTC', 'USDT', 42758.8)
mycursor.execute(sql_insert, values)
# mycursor.execute("INSERT INTO PriceHistory (BaseCurrency, QuoteCurrency, Price) VALUES ('BTC', 'USDT', 42758.8);")
# mycursor.execute("CREATE DATABASE Binance")
# mycursor.execute("SHOW Tables")
# for x in mycursor:
#   print(x) 
# exit(0)
# Open the file in read mode
# with open('/lhome/dsingh_local/Desktop/tradebot/output.txt', 'r') as file:
#     # Iterate over each line in the file
#     for line in file:
#         pass
        # Process the line (replace this with your own logic)
        # btc.append(line.strip().split(" ")[3])  # .strip() removes leading and trailing whitespace
        # sol.append(line.strip().split(" ")[7])  # .strip() removes leading and trailing whitespace
        # matic.append(line.strip().split(" ")[11])  # 
