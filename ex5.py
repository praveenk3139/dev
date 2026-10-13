from pandas import read_csv
from matplotlib import pyplot

# Load the dataset (download daily-min-temperatures.csv from github.com/jbrownlee/Datasets)
series = read_csv('daily-min-temperatures.csv', header=0, index_col=0, parse_dates=True)
print(series.head())

# 1. Line plot
series.plot()
pyplot.title("Daily Minimum Temperatures")
pyplot.show()

# 2. Line plot with dotted style
series.plot(style='-.')
pyplot.show()

# 3. Histogram
series.hist()
pyplot.show()

# 4. Density plot
series.plot(kind='kde')
pyplot.show()