# random game
# random from 1 to 100
import random

MIN = 1
MAX = 100
answer = random.randint(MIN, MAX)
# can input 10 times
COUNT = 1
MAX_COUNT = 10

while COUNT <= MAX_COUNT:
    n = int(input())
    if n <= MIN or n >= MAX:
        continue
    if n == answer:
        print('correct', answer)
        break
    elif n > answer:
        print('input less')
    else:
        print('input big')
    COUNT += 1
else:
    print('count out, answer is ', answer)
