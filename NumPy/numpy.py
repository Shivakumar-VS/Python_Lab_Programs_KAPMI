# 7. Write a Python program to Create array using NumPy and perform array 
# operations. 
import numpy as np  
# Creating an array 
arr = np.array([5, 2, 4, 1, 3, 6])  

# Print the original array 
print("Original Array:") 
print(arr)  

# Array Operations  
# Sum of array elements 
print("\nSum of Array Elements:", np.sum(arr)) 

# Mean of array elements 
print("Mean of Array Elements:", np.mean(arr))

# Maximum element in the array 
print("Maximum Element:", np.max(arr))  

# Minimum element in the array  
print("Minimum Element:", np.min(arr))  

# Sorting the array  
print("\nSorted Array:") 
print(np.sort(arr))  

# Reshaping the array  
reshaped_arr = arr.reshape(2, 3)   
print("\nReshaped Array:") 
print(reshaped_arr)  