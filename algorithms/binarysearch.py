import sys
arr = [11, 13, 24, 26, 35, 37, 46, 49, 54, 68]
print(arr)

target = int(input('please input target'))

n = len(arr)
left = 0
right = n-1

while left <= right:
    center = (left + right)//2
    if arr[center] == target:
        print(center)
        sys.exit()
    elif arr[center] < target:
        left = center + 1
    else:
        right = center -1
print ('not found')