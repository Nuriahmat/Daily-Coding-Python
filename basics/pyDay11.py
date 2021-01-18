# strings
string = input('please input a string:')
print(string[::-1])
# enumerate
for i, ch in enumerate(string):
    print('string[{}] = {}'.format(i, ch))
# split
a, b = input('please a , b: ').split(',')
print('a = ', a)
print('b = ', b)

txt = 'String&int&boolean&list'
after_split = txt.split('&')
print(after_split[0])

# join
join_txt = ('abcd', 'efg', 'hij')
print(''.join(join_txt))
print('->'.join(join_txt))

join_upper = 'ABCDEF'
print('->'.join(join_upper))
