# ジャンケンゲーム
# shitou 0 jianzi 1 bu 2
import random
win = los = equal = 0
while True:
    comp = random.randint(0, 2)
    while True:
        human = int(input('shitou 0 jianzi 1 bu 2'))
        if 0 <= human <= 2:
            break
    print('i am', end=' ')
    if human == 0:
        print('shitou', end=' ')
    elif human == 1:
        print('jianzi', end=' ')
    else:
        print('bu', end=' ')
    print('des')

    judge = (human - comp + 3) % 3
    if judge == 0:
        print('equal')
        equal += 1
    elif judge == 1:
        print('lose')
        los += 1
    else:
        print('win')
        win += 1
    game_out = int(
        input('do you want to exit this game ? yes/1 no/any number'))
    if game_out == 1:
        break
print('game out')
