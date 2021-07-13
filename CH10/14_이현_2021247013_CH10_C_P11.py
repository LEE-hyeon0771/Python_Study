'''
분해 : 근무 시간, 시간당 임금, 주당 근무 시간, 초과 근무 시간, 1.5배 임금, 총 임금
패턴인식 : 사용자로부터 근무 시간과 시간당 임금을 입력받는다.
           주당 근무 시간이 40시간을 넘으면 초과 근무 수당으로 1.5배 임금을 지급한다.
추상화 : 1. input을 사용하여 근무 시간과 시간 당 임금을 입력 받는다.
         2. 근무 시간과 시간 당 임금은 정수 이므로 int로 강제형 변환을 시켜준다.
         3. if 주당 근무 시간 > 40 : 시간당 임금 * 40 + 초과 근무 시간 * 시간당 임금 * 1.5,
            else : 시간당 임금 * 40을 출력한다.
         4. 초과 근무 시간 = 근무시간 - 40 을 선언해 준다.
'''
#알고리즘

time = int(input("근무 시간을 입력하시오: "))
time_money = int(input("시간 당 임금을 입력하시오: "))

over_time = time - 40
total_money = time_money * 40
over_time_total = total_money + over_time * (time_money * 1.5)

if time > 40 :
    print(f"총 임금은 {over_time_total}원 입니다.")
else :
    print(f"총 임금은 {total_money}원 입니다.")
    
