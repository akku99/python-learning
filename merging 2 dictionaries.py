d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1 | d2
print(d3)

# using loop
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d3 = d1.copy()
for key, value in d2.items():
    d3[key] = value
print(d3)

# Usig update
d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}
d1.update(d2)
print(d1)