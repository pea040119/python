print("가로 길이를 입력하세요: ")
width = int(input())
print('세로 길이를 입력하세요: ')
height = int(input())
c = width*2 + height*2
a = width * height
print('직사각형의 둘레:', c)
print('직사각형의 넓이20:', a)

print("첫 번째 숫자를 입력하세요: ")
a = int(input())
print('두 번째 숫자를 입력하세요: ')
b = int(input())
print('두 수의 합:', a+b)
print('두 수의 차:', a-b)
print('두 수의 곱:', a*b)
print('두 수의 나눗셈:', a/b)

print("화씨 온돌르 입력하세요: ")
f = float(input())
print('화씨 온도 %.2f는 섭씨 온도 %.2f' % (f, (f-32)/1.8))
print("섭씨 온돌르 입력하세요: ")
c = float(input())
print('섭씨 온도 %.2f는 섭씨 온도 %.2f' % (c, c*1.8 +32))