import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data & view summary
df = pd.read_csv("winequality.csv")  # Replace with your CSV path
cols = ['alcohol', 'volatile acidity', 'citric acid', 'residual sugar']
print(df.describe())

# 2. Quality count
sns.countplot(x='quality', data=df)
plt.title("Wine Quality Distribution")
plt.show()

# 3. Boxplots & Histograms
for col in cols:
    sns.boxplot(x='quality', y=col, data=df)
    plt.title(f"{col} by Quality")
    plt.show()

    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()

# 4. Pairplot & Correlation Heatmap
sns.pairplot(df, vars=cols, hue='quality', diag_kind='kde')
plt.show()

plt.figure(figsize=(9, 7))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Heatmap")
plt.show()
