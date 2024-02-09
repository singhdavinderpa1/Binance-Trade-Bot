import matplotlib.pyplot as plt
import mysql.connector
from auth import connection

mydb = connection()

sol = []
matic = []
btc = []
# Open the file in read mode
with open('/lhome/dsingh_local/Desktop/tradebot/output.txt', 'r') as file:
    # Iterate over each line in the file
    for line in file:
        # Process the line (replace this with your own logic)
        btc.append(line.strip().split(" ")[3])  # .strip() removes leading and trailing whitespace
        sol.append(line.strip().split(" ")[7])  # .strip() removes leading and trailing whitespace
        matic.append(line.strip().split(" ")[11])  # .strip() removes leading and trailing whitespace

mapping = {"BTC":btc,
           "SOL":sol,
           "MATIC":matic}

mycursor = mydb.cursor()
sql_insert = "INSERT INTO Binance.PriceHistory (Currency, Price) VALUES (%s, %s);"

# Define the values to be inserted
currency = ['BTC', 'SOL', 'MATIC']
for i in currency:
    for val in [float(value) for value in mapping[i]]:
        print(i, val)
        values = (i, val)
        print(mycursor.execute(sql_insert, values))
        mydb.commit()
        

