
a = int(input())
b = int(input())
c = int(input())
if (a+b < c) and (a+c < b) and (b+c < a):
    print('yes')
else:
    print('no')
    
print('원피스의 개수를 입력하시요:')
a = int(input())
print('스웨터의 개수를 입력하시요:')
b = int(input())
t = a*5 + b*3
if t < 10:
    result = int(t*0.95 * 10000)
elif t>=10 and t<20:
    result = int(t*0.9 * 10000)
else:
    result = int(t*0.8 * 10000)
print('총액:', result)

print('숫자를 입력하세요:')
a = int(input())
if (a%10 == 3) or (a%10 == 6) or (a%10 == 9):
    print('yes')
else:
    print('no')
    
print('숫자를 입력하세요:')
a = int(input())
result = 0
while a > 10:
    result += a%10
    a = a//10
    if a < 10:
        result += a
print(result)

print('숫자를 입력하세요:')
a = int(input())
result = 0
for i in range(a+1):
    result += 2**i
print(result)

a = 1
result = 0
while a != 0:
    print('숫자를 입력하세요:')
    a = int(input())
    result += a
print(result)

print("가로 길이를 입력하세요: ")
width = int(input())
print('세로 길이를 입력하세요: ')
height = int(input())
for i in range(height):
    for j in range(width):
        print('*', end= '')
    print()

print('밑변의 길이를 입력하세요:')
a = int(input())
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
