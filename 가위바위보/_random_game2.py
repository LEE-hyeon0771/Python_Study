import random


def rock_si_pa():
    user = 0
    com = 0
    
    while user !=2 and com !=2:
        computer = ["보","가위","바위"]
        com_ans = random.choice(computer)
        com_num = computer.index(com_ans)
        print(f"가위 바위 보에 해당하는 숫자를 입력하세요.")
        user_ans = int(input("0:가위, 1:바위, 2:보 => "))

        print(f"com : {com_ans}")

        if user_ans == com_num :
            print("user_win !!")
            user = user + 1
        elif user_ans - com_num == -1 or user_ans - com_num == 2:
            print("draw!!")
        else:
            print("com_win!!")
            com = com + 1
        if user == 2:
            print(f"최종 결과는 user_win!!")
        elif com == 2:
            print(f"최종 결과는 com_win!!")


print("*"*26)
print("*      가위 바위 보      *")
print("*"*26)
rock_si_pa()
while True:
    keep = input("계속하시겠습니까?(Y/N)")
    if keep == "Y":
        rock_si_pa()
    elif keep == "N":
        print(f"안녕히가세요.")
        break
        
    
        
