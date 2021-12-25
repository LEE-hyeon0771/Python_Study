a,b = input("숫자 두 개를  입력하세요.").split()
a = int(a)
b = int(b)

print(a+b)

#a,b = int(input("숫자 두 개를 입력하세요.")).split()
#print(a+b)
#split()은 문자열과 공백에 해당하는 메소드 이므로 위 처럼 사용 X

a,b = map(int, input("숫자 두 개를 입력하세요.").split(","))
print(a+b)
#map을 활용해서 input을 바로 int로 변환시켜 한 줄로 나타냄

a,b,c = map(int, input().split())
print(a+b+c)

a= 50
b= 100
c= None

print(a)
print(b)
print(c)

a,b,c,d = map(int, input().split())
sum = a+b+c+d
average = sum/4
print(int(average))
