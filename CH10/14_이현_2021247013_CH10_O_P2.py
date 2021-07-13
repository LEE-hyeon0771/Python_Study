'''
분해 : 신장, 체중, BMI
패턴인식 : 신장과 체중을 입력받는다.
           입력 받은 신장과 체중으로 BMI값을 출력한다.
추상화 : 몸무게와 키를 소수점까지 나타내어야 하므로 float으로 강제형변환 시켜준다.
         input을 이용하여 몸무게와 키를 입력받는다.
         BMI공식을 이용하여 BMI를 구하는 방식을 선언한다.
         f-string방식을 사용하여 BMI를 print한다.
'''
#알고리즘

weight = float(input("몸무게를 kg 단위로 입력하시오: "))
height = float(input("키를 미터 단위로 입력하시오: "))

BMI_Chart = weight/(height**2)

print(f"당신의 BMI= {BMI_Chart}")
