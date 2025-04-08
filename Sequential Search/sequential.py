def linear_search(arr, target, size):
    found = False
    for i in range(size):
        if arr[i] == target:
            found = True
            break
    if found:
        print("Number found")
    else:
        print("Number not found")
numbers = []
size = int(input("Enter the size of the list: "))
for i in range(size):
    num = int(input("Enter a number: "))
    numbers.append(num)
target = int(input("Enter the number to search: "))
linear_search(numbers, target, size)