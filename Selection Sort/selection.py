# 2.  Write a Python Program to Implement Selection Sort. 
def selection_sort(arr): 
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(n): 
        # Assume the element at index i is the minimum 
        min_idx = i 
        # Find the minimum element in the remaining unsorted array 
        for j in range(i+1, n): 
            if arr[j] < arr[min_idx]: 
                min_idx = j 
        # Swap the found minimum element with the element at index i 
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
 
# Create an empty list to store the elements 
arr = [] 
 
# Read elements from the keyboard 
n = int(input("Enter the number of elements: ")) 
for _ in range(n): 
    element = int(input("Enter element: ")) 
    arr.append(element) 
 
# Perform selection sort 
selection_sort(arr) 
 
# Print the sorted array 
print("Sorted array:", arr) 