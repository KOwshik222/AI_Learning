import pandas as pd
import numpy as np

# Create a sample dataset (like Titanic)
data = {
    'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Braund, Mr. Owen', 'Cumings, Mrs. John', 'Heikkinen, Miss. Laina', 
             'Futrelle, Mrs. Jacques', 'Allen, Mr. William', 'Moran, Mr. James',
             'McCarthy, Mr. Timothy', 'Palsson, Master. Gosta', 'Johnson, Mrs. Oscar',
             'Nasser, Mr. Nicholas'],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'female', 'male'],
    'Age': [22, 38, 26, 35, 35, np.nan, 54, 2, 27, 14],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.08, 11.13, 30.07],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1, 1, 0]
}

df = pd.DataFrame(data)
print(df)

#SAVE TO CSV FILE 

# Save to CSV file
df.to_csv('titanic_sample.csv', index=False)
print("File saved as 'titanic_sample.csv'")

#LOAD CSV DATA
df = pd.read_csv('titanic_sample.csv')
print(df.head())  #PRINT FIRST ROWS

print(df.tail()) #print bottom rows

print(df.sample(6)) # print random 

print(df.info()) # information of data

print(df.describe()) #statistical information

print(df.dtypes) # about data types



print("----------------------------------practice questions-----------------------------")

data = {
    'PassengerId': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Name': ['Braund, Mr. Owen', 'Cumings, Mrs. John', 'Heikkinen, Miss. Laina', 
             'Futrelle, Mrs. Jacques', 'Allen, Mr. William', 'Moran, Mr. James',
             'McCarthy, Mr. Timothy', 'Palsson, Master. Gosta', 'Johnson, Mrs. Oscar',
             'Nasser, Mr. Nicholas'],
    'Sex': ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'male', 'female', 'male'],
    'Age': [22, 38, 26, 35, 35, np.nan, 54, 2, 27, 14],
    'Fare': [7.25, 71.28, 7.92, 53.10, 8.05, 8.46, 51.86, 21.08, 11.13, 30.07],
    'Survived': [0, 1, 1, 1, 0, 0, 0, 1, 1, 0]}

print(f"total passengers:{len(df)}")

male = df[df['Sex']=='male']
print(f"total males :{len(male)}")