import random
# from 1 to 100 random
MIN = 1
MAX = 100
# 10 times
COUNT = 1
COUNT_MAX = 10

answer = random.randint(MIN, MAX)

while COUNT <= COUNT_MAX:
    n = int(input())
    if n <= 0 or n > 100:
        continue
    if n == answer:
        print('is correct ', answer)
        break
    elif n > answer:
        print('input less')
    else:
        print('input big')
    COUNT += 1
else:
    print('out of count, correct number is', answer)
