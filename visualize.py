import matplotlib.pyplot as plt

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


fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))

limit = -500
# Plot the sol data
data = [float(value) for value in btc]
data = data[limit:]
ax1.plot(data)
ax1.set_title('BTCUSDT')
    
# Plot the sol data
data = [float(value) for value in sol]
data = data[limit:]
ax2.plot(data) 
ax2.legend("haha")
ax2.set_title('SOLEUR')

# Plot the matic data
data = [float(value) for value in matic]
data = data[limit:]
ax3.plot(data)
ax3.set_title('MATICEUR')
# plt.gca().invert_yaxis()
plt.savefig('/lhome/dsingh_local/Desktop/tradebot/MATIC.png')

# for i, ax in enumerate([ax1, ax2, ax3], start=1):
#     filename = f"subplot_{i}.png"
#     ax.figure.savefig(filename)
#     print(f"Saved {filename}")


# Show the plot
# plt.show()