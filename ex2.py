import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load & inspect
df = pd.read_csv("Emaildataset.csv")
print(df.info(), df.head(), df.describe(), df.isnull().sum())

# 1. Pairplot (sample subset to avoid memory crash)
sns.pairplot(df[['the', 'to', 'for', 'Prediction']], hue='Prediction')
plt.show()

# 2. Countplot (Prediction: 0 = Ham, 1 = Spam)
sns.countplot(x='Prediction', data=df)
plt.show()

# 3. Correlation heatmap
sample_cols = ['the', 'to', 'ect', 'for', 'Prediction']
sns.heatmap(df[sample_cols].corr(), annot=True, cmap='coolwarm')
plt.show()

# 4. Word cloud from word frequencies
wc = WordCloud(width=800, height=400).generate_from_frequencies(df.iloc[:, 1:-1].sum())
plt.imshow(wc)
plt.axis('off')
plt.show()
