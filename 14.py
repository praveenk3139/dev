import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('daily-min-temperatures.csv',
                   header=0, index_col=0, parse_dates=True)

print(data.head())

# 1. Line Plot
data.plot()
plt.title("Daily Minimum Temperatures")
plt.show()

# 2. Trend Analysis (Moving Average)
data.rolling(30).mean().plot()
plt.title("Temperature Trend")
plt.show()

# 3. Seasonal Pattern
data.groupby(data.index.month).mean().plot(kind='bar')
plt.title("Monthly Seasonal Pattern")
plt.show()

# 4. Variation (Histogram)
data.hist()
plt.title("Temperature Variations")
plt.show()

# 5. Density Plot
data.plot(kind='kde')
plt.title("Temperature Density")
plt.show()