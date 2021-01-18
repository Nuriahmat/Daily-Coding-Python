import time
# while loop
# from 1 to n sum
n = int(input('please input a number'))
sums = 0
i = 1
while i <= n:
    sums += i
    i += 1
print(sums)

# with break 
## just plus number
while True:
    n = int(input('please enter'))
    if n > 0:
        break
sums2 = 0
j = 1
while j <= n:
    sums2 += j 
    j += 1
print(sums2)

# timer
setTimer = int(input('what time do you want to set timer?'))

while setTimer > 0:
    print(setTimer)
    setTimer -= 1
    time.sleep(1) # sleep 1 secend  
print('times up')