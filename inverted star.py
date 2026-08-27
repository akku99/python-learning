# Using for loop

n = int(input("Enter the number of rows: "))
for i in range(n, 0, -1):
    print((n - i) * ' ' + i * '*')


# Using while loop

n = int(input("Enter the number of rows: "))
i = n
while i > 0:
    print((n - i) * ' ' + i * '*')
    i -= 1


# Using Recursion

def pattern(n, space=0):
    if n > 0:
        print(' ' * space + '*' * n)
        pattern(n - 1, space + 1)
pattern(int(input("Enter the number of rows: ")))