#홀짝게임
'''
다음의 게임을 만드시오.
컴퓨터는 홀/짝이라는 값을 가지고 둘중하나를 선택하게 됩니다.
사용자는 컴퓨터가 답으로 가지고 있는 값을 맞추는 게임입니다.
무리한 도박은 패가망신의 지름길입니다.
게임은 게임일뿐 도박은 금물!!

분해 : 홀짝, 랜덤, 동전, 배팅, 승리보상, 패배의 결과

패턴인식 : 컴퓨터는 홀 or 짝 중에 반드시 한가지를 정답으로 가짐(무작위로)
           사용자는 정답을 홀 or 짝 중에 반드시 한가지를 가진다.
           승리하는 경우 배팅금액 보다 큰 값을 가지게 된다.
           패배하는 경우 배팅금액을 몰수당한다.
           홀짝 게임은 여러개의 동전을 가지고 수행한다.
           
추상화 : 컴퓨터가 홀 or 짝 중에 반드시 한가지를 가짐(정답자로 사용)           
         사용자로부터 정답을 문자로 홀 or 짝을 입력받아서 컴퓨터가 가진 값과 비교
         배팅은 초기 점수 내의 점수로만 입력 받는다.
         처음에 사용자는 초기 점수를 입력한다.
         승리하는 경우 배팅 금액의 5배로 한다.
         패배하는 경우 배팅금액은 몰수 된다.
         게임의 종료는 초기 점수를 모두 잃었을시에 끝난다.
         게임의 종료는 사용자가 그만 둘 때 끝난다.
         게임 중에는 종료할 수 없다.

알고리즘(의사코드)

홀짝 게임의 환영 멘트 출력

사용방법 출력

사용자의 초기 점수 입력(정수로)

배팅 점수 입력(정수)

컴퓨터가 홀/짝을 결정

사용자가 홀 인지 짝인지 결정

if 컴퓨터 답 == 사용자 답:
    배팅 점수를 5배로 증가
    축하메세지 출력
    
else:
    배팅 점수 몰수
    패배의 메세지 출력
계속할건지 묻기

사용자의 점수 보여주기
게임이 끝나면 또 오세요 출력
'''
import random

def welcome_print():
    print("-"*40)
    print(f"   홀짝 게임에 오신것을 환영합니다.")
    print("-"*40)

    print("="*50)
    print(f"  초기 점수를 입력하시고 배팅 점수를 넣으신 후에")
    print(f"  홀과 짝을 선택하시면 당신의 인생이 달라집니다.")
    print("="*50)

welcome_print()

start_score = int(input("초기 점수 입력 : "))
while True:
    print(f"당신의 배팅 가능 점수 : {start_score}")
    while True:
        bet_score = int(input("배팅 점수 입력 : "))
        if start_score < bet_score :
            print(f"배팅 점수가 시작 점수보다 높을 수 없습니다.")
        else :
            start_score = start_score - bet_score
            break

com_ans = random.choice(["홀","짝"])  #홀 짝 중 하나를 랜덤으로 선택하는 메소드
while True:
    while True:
        user_ans = input("홀 or 짝을 선택하세요")
        if user_ans != "홀" and user_ans != "짝":
            print(f"홀 or 짝만 입력하세요~~")
        else:
            break

    if com_ans == user_ans:
        print(f"정답을 맞춘 당신에게 행운이~~")
        start_score = start_score + bet_score * 5
        print(f"현재 금액은 {start_score} 입니다.")
    else:
        print(f"틀렸습니다. 당신은 안될꺼야~~ 또해봐 어디한번~~")
        print(f"현재 금액은 {start_score} 입니다.")
        bet_score = 0
    if start_score == 0:
        print(f"몽땅 잃은 당신 집에가세요")
        break
    else:
        flag = input("계속하시겠습니까?(Y/N입력)")
        if flag == "Y" or flag == "y" or flag == "네":
            continue
        else:
            break
print("지나친 도박은 패가망신의 지름길입니다.")
print(f"당신의 최종 점수는 {start_score}")
    
        
         
