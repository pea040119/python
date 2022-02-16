import random

r = int(input('반지름을 입력하시요:'))
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

x = [0, 0, 0, 0]
y = [0, 0, 0, 0]
for i in range(4):
    print('2차원 공간의 좌표 x', i+1, ', y', i+1, ' 를 입력하세요:', sep='')
    x[i] = int(input())
    y[i] = int(input())
if (y[0] - y[1]) / (x[0] - x[1]) == (y[2] - y[3]) / (x[2] - x[3]):
    print('평행')
else:
    print('평행 X')

a = int(input('x: '))
b = int(input('y = '))
def gcd(a, b):
    if b > a:
        a, b = b, a
    if (a%b) == 0:
            return b
    else:
        return gcd(b, a%b)
print(gcd(a, b))

x = input('x: ')
def print_reverse(a):
    temp = a[::-1]
    print(int(temp))
print_reverse(x)

def generate_numbers():
    numbers = [0, 0, 0]
    for i in range(3):
        numbers[i] = random.randint(0, 9)
    print('뽑힌숫자:', numbers)
    return numbers
def check_numbers(numbers):
    if numbers[0] == numbers[1] and numbers[2] == numbers[1]:
        if numbers[0] == 7:
            score = 5
        else:
            score = 2
    elif numbers[0] == numbers[1] or numbers[2] == numbers[1] or numbers[0] == numbers[2]:
        score = 1
    else:
        score = 0
    return score
def main():
    total = 0
    jackpot = 0
    check = 1
    while check:
        temp = check_numbers(generate_numbers())
        print('점수', temp)
        total += temp
        if temp == 5:
            jackpot += 1
        check = int(input('그만하시려면 0을 계속할려면 1을 입력하세요'))
    print('총 점수:', total, '잭 팟 횟수:', jackpot)
main()

def generate_numbers():
    numbers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            numbers[i][j] = random.randint(0, 9)
    print('뽑힌숫자:', numbers)
    return numbers
def check_numbers(numbers):
    score = 0
    for i in range(3):
        if numbers[0] == numbers[1] and numbers[2] == numbers[1] and numbers[0] == numbers[2]:
            if numbers[0] == 7:
                score = 5
            else:
                score = 2
        elif numbers[0] == numbers[1] or numbers[2] == numbers[1] or numbers[0] == numbers[2]:
            score = 1
        else:
            score = 0
        for i in range(3):
            if numbers[0] == numbers[1] and numbers[2] == numbers[1] and numbers[0] == numbers[2]:
                if numbers[0] == 7: 
                    score = 5
                else:
                    score = 2
            elif numbers[0] == numbers[1] or numbers[2] == numbers[1] or numbers[0] == numbers[2]:
                score = 1
            else:
                score = 0
def main():
    total = 0
    jackpot = 0
    check = 1
    while check:
        temp = check_numbers(generate_numbers())
        print('점수', temp)
        total += temp
        if temp == 5:
            jackpot += 1
        check = int(input('그만하시려면 0을 계속할려면 1을 입력하세요'))
    print('총 점수:', total, '잭 팟 횟수:', jackpot)
