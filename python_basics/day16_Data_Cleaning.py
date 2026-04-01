import pandas as pd
import numpy as np
df = pd.read_csv('python_basics/Titanic-Dataset.csv')
#detecting empty values
print(df.isnull().sum())
print("--------------------------------------#detecting empty value percentage---------------------------")
missing_percentage = (df.isnull().sum()/ len(df)) *100
print(missing_percentage)
print("--------------------# drop empty value rows-----------------------------")
drop = df.dropna()
print(drop)

df_cleaned = df.dropna(subset=['Age'])
print(df_cleaned)

# Drop columns that have >50% missing
threshold = 0.5 * len(df)
df_cleane = df.dropna(thresh=threshold, axis=1)

#outliers - outliers is an observation that lies in abnormal distance from other values in a data set. 
# there are two common methods to detect outliers 1)iqr 2)z-score

#iqr works based on quartiles,works on any type of data,it has a forulmas to detect outliers
#z -score works based on mean and std, works on normal distribution.