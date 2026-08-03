num = int(input("Enter a number: "))
if num < 10:
    print("Not divisible by zero")
else:
    num = num % 100
    num = num // 10
    if num % 3 == 0:
        print("The 2nd last digit is divisible by 3")
    else:
        print("The 2nd last digit is not divisible by 3")