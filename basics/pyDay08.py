n = int(input())
per_line = int(input())
for i in range(n):
    if i > 0 and i % 6 == 0:
        print()
    print('*', end='')
print()
