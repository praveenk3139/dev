import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create sample dataset
np.random.seed(123)
data = pd.DataFrame({
    'ID': range(1, 11),
    'Age': np.random.randint(18, 61, 10),
    'Gender': np.random.choice(['Male', 'Female'], 10),
    'Score': np.random.randint(1, 101, 10)
})
print("Original Data:\n", data)

# ---------- Variable Filters ----------
# 1. Filter by specific value (Age > 30)
filtered_data = data[data['Age'] > 30]
print("\nAge > 30:\n", filtered_data)

# 2. Filter by multiple conditions (Age > 30 AND Gender == 'Male')
filtered_data2 = data[(data['Age'] > 30) & (data['Gender'] == 'Male')]
print("\nAge > 30 & Male:\n", filtered_data2)

# ---------- Row Filters ----------
# 1. Remove duplicate rows & 2. Remove missing values (NA)
cleaned_data = data.drop_duplicates(subset=['ID']).dropna()
print("\nCleaned Data:\n", cleaned_data)

# ---------- Data Visualization ----------
# Scatterplot: Age vs Score colored by Gender
sns.scatterplot(data=cleaned_data, x='Age', y='Score', hue='Gender', s=100)
plt.title("Scatterplot of Age vs. Score")
plt.show()

# Histogram: Age distribution
sns.histplot(data=cleaned_data, x='Age', binwidth=5, color='blue', alpha=0.5)
plt.title("Histogram of Age")
plt.show()

# Bar chart: Gender distribution
sns.countplot(data=cleaned_data, x='Gender', palette=['green', 'purple'])
plt.title("Gender Distribution")
plt.show()