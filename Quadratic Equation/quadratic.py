# Python program to solve quadratic equation_roots
import math
def equation_roots(a,b,c):
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    if dis > 0:
        print("Real and different roots:")
        root1 = (-b + sqrt_val)/(2*a)
        root2 = (-b - sqrt_val)/(2*a)
        print("Root1 = ", root1)
        print("Root2 = ", root2)
    elif dis == 0:
        print("Real and same roots:")
        root1 = root2 = -b / (2 * a)
        print("Root1 = Root2 =", root1)
    else:
        print("Complex roots:")
        real_part = -b / (2 * a)
        imaginary_part = sqrt_val / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        print("Root1 =", root1)
        print("Root2 =", root2)
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    equation_roots(a, b, c)