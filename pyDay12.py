# str
txt = input('txt: ')
ptn = input('ptn: ')

if ptn in txt:
    print('ptn included in txt')
else:
    print('ptn not included in txt')

for ch in txt:
    print(ch, end='->')
print()

for rh in txt[::-1]:
    print(rh, end=' ')
print()

find_txt = input('find_txt: ')
target = input('target: ')
print(find_txt.find(target))
print(find_txt.rfind(target))
print(find_txt.index(target))
print(find_txt.rindex(target))
