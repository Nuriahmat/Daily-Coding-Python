# list
list01 = [1, 2, 3, 4, 5]
list01.insert(2, 6)
list01.remove(1)
print(list01)
print(list01.index(2))
list01.clear()
print(list01)
# insert
in_list = ['a', 'b', 'c', 'd', 'e']
in_list.insert(2, 'f')
## ['a', 'b', 'f', 'c', 'd', 'e']
# remove
re_list = ['a', 'b', 'c', 'd', 'e']
re_list.remove('b')
## ['a', 'c', 'd', 'e']
# del
del_list = ['a', 'b', 'c', 'd', 'e']
del del_list[0]
## ['b', 'c', 'd', 'e']
# clear
clear_list = ['a', 'b', 'c', 'd', 'e']
clear_list.clear()
# []
# reverse
rev_list = ['a', 'b', 'c', 'd', 'e']
rev_list.reverse()
## ['e', 'd', 'c', 'b', 'a']
# index
index_list = ['a', 'b', 'c', 'd', 'e']
index_list.index('b')
# 1
# pop
pop_list = ['a', 'b', 'c', 'd', 'e']
y = pop_list.pop(1)
## y == b
##del_list = ['a', 'c', 'd', 'e']
# append
app_list = ['a', 'b', 'c', 'd', 'e']
app_list.append('h')
##['a', 'b', 'c', 'd', 'e', 'h']
# extand
x = ['a', 'w', 'e']
y = ['z', 'x', 'c']
x += y  # ['a', 'w', 'e', 'z', 'x', 'c']
x.extend(y)  # ['a', 'w', 'e', 'z', 'x', 'c']
