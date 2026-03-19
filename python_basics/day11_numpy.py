#A NumPy array is a homogeneous (same type) contiguous (next to each other) block of memory with metadata about its shape and type.
import numpy as np
arr = np.array([1,2,3,4])
print(arr)
print(arr.shape)
print(len(arr))
print(arr.shape)
print("-----------------------------------------------------------------------------------------")
zeros = np.zeros(6)
print(zeros)
zeros = np.zeros((3,2))
print(zeros)
ones = np.ones(6)
print(ones)
ones = np.ones(
    (3,2)
)
print(ones)
print("-------------------------------------RANGE OF NUMBERS----------------------------------------------")
arr = np.arange(10)
print(arr)
arr = np.arange(5,10)
print(arr)
arr = np.arange(1,10,3)
print(arr)
print("-----------------------------------RANDOM FUNCTION------------------------------------------")
arr = np.random.rand(5)
print(arr)

arr = np.random.randint(5,100,6)
print(arr)

print("----------------------------------------BASIC OPERATIONS--------------------------------------")

base_price = np.array([100,200,300,400,500])
with_taxes = base_price * 1.1
with_discount = base_price - 20
doubled_price = base_price ** 2
special_price = base_price[1]-20
special_price2 = base_price[1:4]-20
print(with_taxes)
print(with_discount)
print(doubled_price)
print(special_price)
print(special_price2)
print("-------------------------------MUL AND DIV------------------------------")
quantity = np.array([1,2,3,4,5])
price = np.array([100,200,300,400,500])
total_price = quantity*price
print(total_price)
per_person = total_price / 2
print(per_person)
print("----------------------------------ARRAY INFORMATION----------------------------------")

data = np.array([[1,2,3],[4,5,6]])
print(data)
print(data.shape)
print(data.size)
print(data.ndim)
print(data.dtype)
print(data.sum())
print(data.mean())
print(data.min())
print(data.max())
print("---------------------------------- SLICING (Getting Specific Parts)------------------------------")

data = np.array([[10,20,30,40],[50,60,70,80],[90,90,100,110]])
print(data)
print(data[0])
print(data[1])
print(data[[0,1]])
print("-----------------------------------important math operations--------------------------------------------")
scores = np.array([[85, 90, 88],
                   [78, 92, 85],
                   [90, 85, 92]])

print("Student scores (3 students, 3 subjects):")
print(scores)

# Mean (average)
total_avg = scores.mean()
print(f"\nAverage of all scores: {total_avg:.3f}")

# Column means (each subject average)
subject_avg = scores.mean(axis=0)
print(f"Each subject average: {subject_avg}")

# Row means (each student average)
student_avg = scores.mean(axis=1)
print(f"Each student average: {student_avg}")

# Sum
print(f"\nTotal of all scores: {scores.sum()}")
print(f"Sum of each subject: {scores.sum(axis=0)}")
print(f"Sum of each student: {scores.sum(axis=1)}")

# Find highest and lowest
print(f"\nHighest score: {scores.max()}")
print(f"Lowest score: {scores.min()}")
print(f"Range: {scores.max() - scores.min()}")

print("---------------------------------reshaping---------------------------------------")

data = np.array([1,2,3,4,5,6,7,8,9])
arrange_shape = data.reshape((3,3))
print(arrange_shape)


#What is Broadcasting?
#Simple Explanation:
#When you try to add different sized arrays, NumPy automatically stretches the smaller one to match.

print("------------------------------------REAL LIFE ---------------------------------")

data = np.array([[25, 50000, 2],
                 [30, 80000, 5],
                 [35, 120000, 10]])
means = data.mean(axis=0)
print(f"means of the 3:{means}")
