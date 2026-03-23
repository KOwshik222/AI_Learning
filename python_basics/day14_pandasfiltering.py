import pandas as pd
import numpy as np

# Create sample data
data = {
    'Name': ['John', 'Emma', 'Sam', 'Lisa', 'Raj', 'Priya', 'Alex', 'Maya'],
    'Age': [25, 28, 22, 30, 26, 24, 29, 27],
    'Salary': [50000, 60000, 45000, 70000, 55000, 48000, 62000, 53000],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi', 'Mumbai', 'Chennai', 'Delhi', 'Mumbai'],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT']
}

df = pd.DataFrame(data)
print("EMPLOYEE DATASET:")
print(df)

print("--------------------------single condition filtering-----------------------------")
print(df[df['Age']>25])
print(df[df['City']=='Delhi'])

print("=" *20 + "multi condition filtering" + "="*20)
result = df[(df['Age'] > 25) & (df['City'] == 'Delhi')]
print(result)

print(df[(df['City'] == 'Delhi') | (df['City'] == 'Mumbai')])


f = pd.DataFrame({
    'Name': ['John', 'Emma', 'Sam'],
    'Age': [25, 28, 22]
}, index=['row1', 'row2', 'row3'])  # Custom index labels

print(f)
print(f.loc['row1']) # loc is use3d for labels 
print(f.loc['row2'])
print("=======================iloc(used for index)=================================")
print(f.iloc[0])