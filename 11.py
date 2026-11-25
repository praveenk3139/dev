import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("winequality-red.csv", sep=';')
features = ['alcohol', 'volatile acidity', 'citric acid', 'residual sugar']

for f in features:
    sns.histplot(data[f], kde=True)
    plt.title("Histogram - " + f)
    plt.show()

    sns.kdeplot(data[f], fill=True)
    plt.title("Density Plot - " + f)
    plt.show()

    sns.boxplot(y=data[f])
    plt.title("Box Plot - " + f)
    plt.show()