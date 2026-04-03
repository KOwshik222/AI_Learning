import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
data = np.array([[10],[20],[30],[40],[1000]])
MIN_scaler = MinMaxScaler()
scaled = MIN_scaler.fit_transform(data)
std_scaler = StandardScaler()
std_scaled = std_scaler.fit_transform(data)
print(scaled)
print(f"mean of the array is {std_scaler.mean_}")
print(std_scaled)

print("--------------------ENCODING--------------------------------------------")

from sklearn.preprocessing import LabelEncoder
colors = ['red','green','blue']
le = LabelEncoder()
encoded = le.fit_transform(colors)
print(encoded)