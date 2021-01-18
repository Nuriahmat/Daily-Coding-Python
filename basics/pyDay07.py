# for
n = int(input())
for i in range(n):
    print(i, end=' ')
print()

# from 1 to 12 and skip 8
# not use list
for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()

# use list
for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()

for _ in range(10):
    print('*', end='')
print()

print('*' * 40)
for i in range(1, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i * j), end='')
    print()
print('*' * 40)

print('+' * 50)

# rectangle

hight = int(input('enter height:'))
width = int(input('enter width'))

for _ in range(hight):
    for _ in range(width):
        print('*', end='')
    print()
