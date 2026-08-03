# Using iterative approach

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [10, 23, 45, 70, 11, 15, 78, 94]
x = 78
res = linear_search(arr, x)

if res != -1:
    print("Element is present at index", res)
else:
    print("Element is not present in array")


# Using recursive approach

def linear_search_recursive(arr, x, i=0):
    if i == len(arr):
        return -1
    if arr[i] == x:
        return i
    return linear_search_recursive(arr, x, i + 1)

arr = [10, 23, 45, 70, 11, 15, 78, 94]
x = 11
res = linear_search_recursive(arr, x)

if res != -1:
    print("Element is present at index", res)
else:
    print("Element", x, "is not present in array")