import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('Titanic-Dataset.csv')
print(df.head())
print(df.columns.tolist())
plt.figure(figsize=(8,5))
sns.histplot(df['Age'].dropna(),bins = 30 ,kde=False)
plt.title('Age Distribution')
plt.xlabel('Age (years)')
plt.ylabel('numver of passengers')
plt.show()
data = pd.read_csv('Titanic-Dataset.csv')
plt.figure(figsize=(6,4))
sns.boxplot(x=data['Fare'])
plt.title('Fare Boxplot')
plt.xlabel('Fare in currency')
plt.show()


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('your_file.csv')  # change to your file

# Quick overview of all numeric columns
df.hist(bins=30, figsize=(15,10))
plt.show()

# Correlation heatmap
sns.heatmap(df.corr(), annot=True)
plt.show()

# Pairplot (if you have few columns)
sns.pairplot(df)
plt.show()