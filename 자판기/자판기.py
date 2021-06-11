def print_menu():
    print("*"*24)
    print(" "*2, "음료수 자판기 메뉴")
    print("*"*24)
    print(" 1. 데  자  와 :  500원")
    print(" 2. 북두사이다 :  700원")
    print(" 3. 봉      봉 :  800원")
    print(" 4. 코  코  팜 :  900원")
    print(" 5. 밀  키  스 : 1100원")
    print(" 6. 콜      라 : 1500원")
    print(" 7. 에  비  앙 : 2000원")
    print()
def input_money(money):
    print("-----돈을 투입하세요-----")
    _1000won = int(input("1000원(장): "))
    _500won = int(input("500원(개): "))
    _100won = int(input("100원(개): "))
    money = money + _1000won * 1000 + _500won * 500 + _100won * 100
    print(f"투입금액 : {money}")
    return money
def able_menu(money):
    print("-----구입 가능한 음료 메뉴-----")
    if money >= 2000:
        print("1. 데자와 2. 북두사이다 3. 봉봉 4. 코코팜 5. 밀키스 6. 콜라 7.에비앙")
        return 7
    elif money >=1500:
        print("1. 데자와 2. 북두사이다 3. 봉봉 4. 코코팜 5. 밀키스 6. 콜라")
        return 6
    elif money >=1100:
        print("1. 데자와 2. 북두사이다 3. 봉봉 4. 코코팜 5. 밀키스")
        return 5
    elif money >=900:
        print("1. 데자와 2. 북두사이다 3. 봉봉 4. 코코팜")
        return 4
    elif money >=800:
        print("1. 데자와 2. 북두사이다 3. 봉봉")
        return 3
    elif money >=700:
        print("1. 데자와 2. 북두사이다")
        return 2
    else:
        print("1. 데자와")
        return 1  #데자와 번호가 1임

def sel_menu(select, money):
    if select == 1:
        print("데자와를 드립니다.")
        return money - 500
    elif select == 2:
        print("북두사이다를 드립니다.")
        return money - 700
    elif select == 3:
        print("봉봉을 드립니다.")
        return money - 800
    elif select == 4:
        print("코코팜을 드립니다.")
        return money - 900
    elif select == 5:
        print("밀키스를 드립니다")
        return money - 1100
    elif select == 6:
        print("콜라를 드립니다.")
        return money - 1500
    elif select == 7:
        print("에비앙을 드립니다.")
        return money - 2000

def check_flag(cn_flag):
    if cn_flag !='y' and cn_flag != "Y" and cn_flag != 'n' and cn_flag !="N":
        return True
    else:
        return False

def give_change(money):
    print()
    print(f"잔돈 {money}원")
    print("-----거스름 돈 반환-----")
    if money >=1000:
        print("1000원 : 1장")
        money = money - 1000
        print(f"500원 : {money//500}개")
        money = money % 500
        print(f"100원 : {money//100}개")
        money = money % 100
    else:
        print(f"500원 : {money//500}개")
        money = money % 500
        print(f"100원 : {money//100}개")
        money = money % 100
print_menu()
money = 0
while True:
    money = input_money(money)
    if money < 500:
        print("구매할 수 있는 음료가 없습니다.")
        print("돈을 더 투입하시기 바랍니다.")
        continue
    break

while True:
    able_num = able_menu(money)
    select = int(input("메뉴 선택>>"))
    if select > able_num or select < 1:       
        print("구매 가능한 음료가 없습니다.")       #able_num의 return 숫자
    else:
        money = sel_menu(select,money)
        print(f"잔액 : {money}원")
    if money < 500:
        print("잔액이 부족하여 거스름돈을 드립니다.")
        break
    while True:      #500원 이상 남을 경우 계속 자판기를 이용하게 해주는 방법
        cn_flag = input("자판기를 계속 이용하시겠습니까?(Y/N)")
        if check_flag(cn_flag):
            print("Y/N으로만 입력하세요")
            continue
        break
    if cn_flag == 'Y' or cn_flag == 'y':
        continue #알고리즘 4번으로 돌아가 입력받은 금액보다 적거나 같은 음료수 메뉴들을 출력해줌
    break

give_change(money)
    
