d = {'a': 100, 'b': 200, 'c': 300}
res = sum(d.values())
print(res)

# using list comprehension

d= d = {'a': 100, 'b': 200, 'c': 300}
res = sum([d[key] for key in d])
print(res)

# using for loop
d = {'a': 100, 'b': 200, 'c': 300}
res = 0
for value in d.values():
    res += value
print(res)

