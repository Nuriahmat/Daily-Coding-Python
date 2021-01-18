h = int(input('hight:'))
# 1
for i in range(1, h + 1):
    print('*' * i)
# 2
for j in range(h + 1):
    print('*' * (h - j))
# 3
for k in range(h):
    for _ in range(h - k - 1):
        print(' ', end='')
    for _ in range(k + 1):
        print('*', end='')
    print()
