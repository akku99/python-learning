"""
# 1. ********* Using While Loop 
This program calculates the factorial of a given number using a while loop.
"""

num = int(input("Enter a number: "))

factorial = 1

while num > 0:
    factorial = factorial * num
    num = num -1

print(f"The factorial of the given number is: {factorial}")


# 2. ********* Using for Loop *********

num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num+1):
    factorial *= i

print(f"The factorial of the given number is: {factorial}")



# 3. ********* Using Function *********

def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"

    factorial = 1
    while n > 0:
        factorial = factorial * n
        n = n - 1
    return factorial

numbers = [0,1,5,7]

for num in numbers:
    result = factorial_iterative(num)
    print(f"Factorial of {num} is: {result}")