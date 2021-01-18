#Month
month = int(input('please inter a number '))

if month in {3, 4, 5}:
    print('spring')
elif month in {6, 7, 8}:
    print('summer')
elif month in {9, 10, 11}:
    print('ant')
elif month in {12, 1, 2}:
    print('k')
else:
    print('something else')

#plus minus zero 
a = int(input('number a:'))
print('this is '+('plus' if a > 0 else '0' if a == 0 else 'minus'))

#even number and odd number
n = int(input('please input a number'))
if n >= 0:
    if n % 2 == 0:
        print('even number')
    else:
        print('odd number')
else:
    print('input a plus number')

# min number and max number
x = int(input('input x:'))
y = int(input('input y:'))
    #style1
if x > y:
    minNumber = y
    maxNumber = x
else:
    minNumber = x
    maxNumber = y
print('min Number is',minNumber)
print('max Number is',maxNumber)

    #style2
minNumber,maxNumber = (x, y) if y > x else (y, x)
print('min Number is',minNumber)
print('max Number is',maxNumber)
    #style3
minNumber = min(x, y)
maxNumber = max(x, y)
print('min Number is',minNumber)
print('max Number is',maxNumber)