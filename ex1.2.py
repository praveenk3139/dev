import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("CountryData.csv")
plt.hist(data['income'])
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()
