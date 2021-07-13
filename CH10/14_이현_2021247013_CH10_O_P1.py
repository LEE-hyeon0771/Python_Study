'''
분해 : 사과, 배, 멜론, 가격, 과일 총액
패턴인식 : 사과는 개당 1000원, 배는 개당 2000원, 멜론은 개당 3000원이다.
           사과를 10% 할인해서 판매한다.
           과일 총액을 계산한다.
추상화 : input을 사용하여 사과, 배, 멜론의 갯수를 입력한다.
         사과, 배, 멜론 갯수의 경우 정수이므로 int로 강제형변환을 시켜준다.
         사과, 배, 멜론의 금액을 곱하여 정확한 가격을 선언해 준다.
         총액을 계산하기 위해 사과+배+멜론 (가격)을 선언해준다.
         총액을 계산할 때 정수를 출력해야 하므로 total 앞에 int를 붙여 강제형 변환을 시켜준다.
         f-string 방식으로 전체금액을 print 해준다.
'''
#알고리즘

apple = int(input("사과 갯수를 입력하세요: "))
pear = int(input("배 갯수를 입력하세요: "))
melon = int(input("멜론 갯수를 입력하세요: "))

apple_money = apple*1000*0.9
pear_money = pear*2000
melon_money = melon*3000
total = apple_money + pear_money + melon_money
total = int(total)

print(f"전체 금액은: {total}")
