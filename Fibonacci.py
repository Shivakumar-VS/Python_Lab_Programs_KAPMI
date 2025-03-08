#program to check if a number is a Fibonacci number or not
a = int(input("Enter a number: "))

c = 0
b = 1
a = 1
#check if the number is 0 or 1
if n == 0 or n == 1:
    Print("Yes")
else:
    while c < n:
        c = a + b
        b = a
        a = c
    if c == n:
        print(f"{n}, Belongs to Fibonacci Sequence")
    else:
        print(f"{n}, Does not belongs to Fibonacci Sequence")