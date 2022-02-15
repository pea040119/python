print('반지름을 입력하시요:')
r = int(input())
PI = 3.14
print('원의 둘레: %.2f' %(2*r*PI))
print('원의 넓이: %.2f' %((r**2)*PI))

print('두 정수를 입력하세요: ')
a = int(input())
b = int(input())
print('%d/%d의 몫은 %d입니다.' % (a, b, a//b))
print('%d/%d의 나머지는 %d입니다.' % (a, b, a%b))

print('2차원 공간의 좌표 (x, y)를 입력하세요:')
x = int(input())
y = int(input())
quadrant = [0, 0, 0, 0]
if x*y > 0:
    if x > 0:
        quadrant[0] = 1
    else:
        quadrant[2] = 1
elif x*y < 0:
    if x > 0:
        quadrant[3] = 1
    else:
        quadrant[1] = 1
for i in quadrant:
    if i == 1:
        print('*(%d, %d)는 %d사분면에 속합니다.' %(x, y, i+1))
    else:
        print('*(%d, %d)는 %d사분면에 속하지 않습니다.' %(x, y, i+1))

