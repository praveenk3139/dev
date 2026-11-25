import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load the dataset
df = pd.read_csv("Emaildataset.csv")

# Basic exploration
print(df.info())
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Spam vs ham count
sns.countplot(x='label', data=df)
plt.title("Spam vs Ham Emails")
plt.show()

# Correlation heatmap (numeric columns only)
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()

# Word cloud of email text
text_data = ' '.join(df['text'])
wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text_data)
plt.figure(figsize=(10, 7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis('off')
plt.show()
