
a = int(input())
b = int(input())
c = int(input())
if (a+b < c) and (a+c < b) and (b+c < a):
    print('yes')
else:
    print('no')
    
a = int(input('원피스의 개수를 입력하시요:'))
b = int(input('스웨터의 개수를 입력하시요:'))
t = a*5 + b*3
if t < 10:
    result = int(t*0.95 * 10000)
elif t>=10 and t<20:
    result = int(t*0.9 * 10000)
else:
    result = int(t*0.8 * 10000)
print('총액:', result)

a = int(input('숫자를 입력하세요:'))
if (a%10 == 3) or (a%10 == 6) or (a%10 == 9):
    print('yes')
else:
    print('no')
    
a = int(input('숫자를 입력하세요:'))
result = 0
while a > 10:
    result += a%10
    a = a//10
    if a < 10:
        result += a
print(result)

a = int(input('숫자를 입력하세요:'))
result = 0
for i in range(a+1):
    result += 2**i
print(result)

a = 1
result = 0
while a != 0:
    a = int(input('숫자를 입력하세요:'))
    result += a
print(result)

width = int(input("가로 길이를 입력하세요: "))
height = int(input('세로 길이를 입력하세요: '))
for i in range(height):
    for j in range(width):
        print('*', end= '')
    print()

a = int(input('밑변의 길이를 입력하세요:'))
for i in range(a+1):
    for j in range(a-i):
        print(' ', end='')
    for j in range(i):
        print('* ', end='')
    print()
for i in range(1, a):
    for j in range(i):
        print(' ', end='')
    for j in range(a-i):
        print('* ', end='')
    print()
