# Using count()

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
print(a.count(1))

# Using Loop
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
count = 0
for val in a:
    if val == 3:
        count += 1
print(count)

# Using operator.countOf()
import operator
a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]
print(operator.countOf(a,9))
