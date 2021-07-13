'''
분해 : 분, 초
패턴인식 : 초 단위의 시간을 입력 받는다
           몇 분 몇 초 인지를 계산한다.
추상화 : input을 사용하여 초단위의 시간을 입력 받는다.
         초 단위의 시간이 정수값이므로 int를 사용하여 강제형 변환을 시켜준다.
         f-string 방식을 사용하여 분과 초를 print한다.
'''
# 알고리즘

time = int(input("초 단위 시간을 입력하세요: "))
sec = time%60
min = time//60

print(f"{min} 분 {sec} 초")
      
