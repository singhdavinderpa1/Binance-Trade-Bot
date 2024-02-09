import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from ast import literal_eval

# Your historical data
data_strings = []
with open('/lhome/dsingh_local/Desktop/tradebot/outputvis.txt', 'r') as file:
    # Iterate over each line in the file
    doc = file.readlines()
    data_strings = doc[-1]
        # Process the line (replace this with your own logic)
        # data.append(line.strip().split(" ")[-1])  # .strip() removes leading and trailing whitespace
print(data_strings, type(data_strings))
# Convert strings to floats
data_floats = [float(value) for value in literal_eval(data_strings)]

# Create a time index
index = pd.date_range(start='2022-01-01', periods=len(data_floats), freq='D')

# Create a pandas DataFrame
df = pd.DataFrame({'Value': data_floats}, index=index)

# Fit an ARIMA model
model = ARIMA(df, order=(1, 1, 1))
result = model.fit()

# Forecast the next values
forecast_steps = 10  # Adjust this as needed
forecast = result.get_forecast(steps=forecast_steps)
forecast_index = pd.date_range(start=df.index[-1] + pd.DateOffset(1), periods=forecast_steps, freq='D')
forecast_values = forecast.predicted_mean.values

# Plot the historical data and forecast
plt.plot(df.index, df['Value'], label='Historical Data')
plt.plot(forecast_index, forecast_values, label='Forecast', linestyle='dashed', color='red')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Print the forecasted values
print('Forecasted Values:')
print(forecast_values)