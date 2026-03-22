print("-------------------------PANDA (SERIES)SINGLE COLUMN-----------------------------")
import pandas as pd
scores = pd.array([1,2,3,4,5])
print(scores)

score = pd.Series([1,2,3,4,],index=['a','b','c','d'])
print(score)

print(score['a'])
print(score['b'])
print(score['c'])
print(score.iloc[1])
print(score[['a','b']])
#Series Operations
print(score+5)
print(score-5)
print(score*5)
print(score/5)
print(score.mean())
print(score.max())
print(score.min())

print("-----------------------DataFrame = Whole table (multiple columns)----------------------------------------")

data = {
    'name':['1','b','c'],
    'age':[10,11,12],
    'marks':[20,21,22]
    }
df = pd.DataFrame(data)
print(df)

#Method 2: From List of Lists
data = [['Alice', 20, 85],
        ['Bob', 22, 90],
        ['Charlie', 21, 88],
        ['David', 23, 92]]
df = pd.DataFrame(data,columns=['name','age','marks'])
print(df)
# First 2 rows
print(df.head(2))

# Last 2 rows
print(df.tail(2))

# Information about dataframe
print(df.info())

# Basic statistics
print(df.describe())

# Column names
print(df.columns)

# Shape (rows, columns)
print(df.shape)  # (6, 4)

# Data types
print(df.dtypes)
condition = df['marks']>88
print(condition)

print("-------------------------opening files----------------------------------")

# Read CSV file
df = pd.read_csv('titanic.csv') 
# Quick look
print(df.head())
print(df.info())
print(df.describe())

# Save to CSV
df.to_csv('output.csv', index=False)