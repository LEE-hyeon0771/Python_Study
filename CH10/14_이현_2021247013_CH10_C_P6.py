'''
분해 : 마트, 사과, 구매, 신선도, 개당 가격
패턴인식 : 사과가 신선하면 마트에서 사과를 산다.
           사과가 개당 1000원 미만이면 10개 구매, 개당 1000원 이상이면 5개 구매한다.
추상화 : 1. input을 이용하여 사과의 상태를 입력받는다.
         2. input을 사용하여 사과 1개의 가격을 입력한다.
         3. 사과 1개의 가격은 정수이므로 int로 강제형 변환을 시켜준다.
         4. if 신선 : 사과 구매 if : 1000원이상 5개 구매 else : 10개 구매, else : 사과 구매x
         
'''
#알고리즘

condition = input("사과의 상태를 입력하시오: ")

if condition == "신선":
    price = int(input("사과 1개의 가격을 입력하시오: "))
    if price >= 1000:
        print(f"사과를 5개 산다.")
    else :
        print(f"사과를 10개 산다.")
else :
    print(f"사과를 사지 않는다.")
