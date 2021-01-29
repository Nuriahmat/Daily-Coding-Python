def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [1, 45, 90, 48, 120, 11]
x = 48
print(search(arr, x))
