string = input('input strings: ')
char = input('input a char: ')

for i in range(len(string)):
    if string[i] == char:
        print('included')
        break
else:
    print('dose not include')
