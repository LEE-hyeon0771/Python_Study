'''
분해 : 햄버거 가게 메뉴 선택 시스템, print_menu()함수, check_menu()함수, print_menu함수는 입력값, 반환값 없음
       check_menu함수는 입력값만 존재, if else구문

패턴인식 : 메뉴를 1,2,3,4번으로 출력한다.
           출력된 메뉴중 선택할 메뉴의 번호를 입력한다.
           1~4번 메뉴 중 선택하면 그 메뉴가 선택되었다는 문구를 출력함
           1~4번 메뉴 중 선택하지 않을 시 잘못된 메뉴를 선택했다는 문구를 출력함
           print_menu 함수는 입력값과 반환값이 존재 하지 않음
           check_menu 함수는 입력값만 존재함

추상화 : print_menu함수 안에 1,2,3,4번 메뉴를 출력한다.
         check 메뉴안에 if else 구문을 활용하여 입력받은 번호가 1~4번 메뉴 중 선택되었는지를 확인한다.
         int와 input을 활용하여 번호를 입력받는다.
         print_menu()와 check_menu()를 호출하여 출력한다.

알고리즘(의사코드)

def print_menu():
    1,2,3,4 메뉴 출력

def check_menu(메뉴번호):

    if 메뉴번호 > 4:
        잘못된 메뉴를 선택하셨습니다. 출력
    else:
        (메뉴번호)번 메뉴가 선택되었습니다. 출력

print_menu()

메뉴번호 입력받기

check_menu()

'''
#자동화
def print_menu():
    
    print(f"1. 치즈버거 세트")
    print(f"2. 불고기버거 세트")
    print(f"3. 치킨버거 세트")
    print(f"4. 종료")

def check_menu(num):
    if num > 4:
        print(f"잘못된 메뉴를 선택하셨습니다.")
    else:
        print(f"{num}번 메뉴가 선택되었습니다.")

print_menu()

num = int(input("메뉴 선택: "))

check_menu(num)
