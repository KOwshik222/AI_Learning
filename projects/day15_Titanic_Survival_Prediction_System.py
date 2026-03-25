import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('projects/Titanic-Dataset.csv')
print("Dataset Loaded")
print(df.head())

print("=================================2(explore the data)================================================")
#print the shape 
print (f"shape of the dataset{df.shape}")

# print info of the dataset
print(f"info of the dataset{df.info}")

#describe about the data
print(f"stats about the dataset{df.describe()}")

print("-------------------------# Check for missing values-------------------------")
print(f"missing values {df.isnull().sum() }")

print("======================================3(cleaning the data)===========================================")

# Drop columns that won’t help prediction (adjust based on your dataset)
# Common columns to drop: 'Cabin', 'Ticket', 'Name', 'PassengerId' (but keep if you want)
df.drop(['Cabin', 'Ticket', 'Name', 'PassengerId'], axis=1, inplace=True, errors='ignore')  # inplace= true means remive permanently 
df.info()# to check dataset is cleaned or not 

# Fill missing Age with median (safe choice)
df['Age']=df['Age'].fillna(df['Age'].median())

# Fill missing Embarked with most frequent value (mode)
df['Embarked']=df['Embarked'].fillna(df['Embarked'].mode()[0])
# Convert categorical columns to numbers
# Sex: male=0, female=1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
# Embarked: S=0, C=1, Q=2 (if present)
df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
# Check if any missing values remain
print(df.isnull().sum())

print("====================================4: Basic Analysis & Visualizations===============================")

# Survival rate by gender
print("Survival rate by gender:")
print(df.groupby('Sex')['Survived'].mean())

print("\nSurvival rate by class:")
print(df.groupby('Pclass')['Survived'].mean())

plt.figure(figsize=(8,5))
sns.histplot(data=df, x='Age', hue='Survived', kde=True, bins=30)#bins refers to number of bars,sns.histplot is used for plotting and histogram
plt.title('Age Distribution by Survival')
plt.show()

sns.barplot(x='Pclass', y='Survived', hue='Sex', data=df)
plt.title('Survival Rate by Class and Gender')
plt.show()
# Save cleaned data
df.to_csv('titanic_cleaned.csv', index=False)