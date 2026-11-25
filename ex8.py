import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("winequality-red.csv", sep=';')

print(data.head())
print(data.info())
print(data.describe())

# Wine quality distribution
sns.countplot(data=data, x='quality')
plt.show()

# Box plot
features = ['alcohol', 'volatile acidity', 'citric acid']
for f in features:
    sns.boxplot(data=data, x='quality', y=f)
    plt.show()

# Pair plot
sns.pairplot(data, vars=features, hue='quality')
plt.show()

# Correlation heatmap
sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.show()

# Histograms
data[features].hist(figsize=(8, 6))
plt.show()