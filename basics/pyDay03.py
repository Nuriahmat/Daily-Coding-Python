# 2 sort
##style1
a = int(input('a:'))
b = int(input('b:'))
if a > b:
    t = a
    a = b
    b = t
print('sorted')
print(a)
print(b)
##style2
a1 = int(input('a1:'))
b1 = int(input('b1:'))
if a1 > b1: a1, b1 = b1, a1
print(a1)
print(b1)

# 3 sort
x = int(input('x:'))
y = int(input('y:'))
z = int(input('z:'))
if x > y: x, y = y, x
if y > z: y, z = z, y
if x > y: x, y = y, x
print('third sorted')
print(x)
print(y)
print(z)