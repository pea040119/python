import random

x = random.randint(1, 100)
while True:
    n = int(input('n:'))
    if n > x:
        print('down')
    elif n < x:
        print('up')
    else:
        break
print('success')


def game():
    x = random.sample(range(0, 10), 3)
    c = 0
    while c < 10:
        n = []
        ball = 0
        strike = 0
        c += 1
        print('***BASEBALL GMAE....ROUND:', c)
        for i in range(3):
            n.append(int(input('number:')))
        for i in range(3):
            if n[i] in x:
                if x[i] == n[i]:
                    strike += 1
                else:
                    ball += 1
        print('ball:', ball, 'strike:', strike)
game()