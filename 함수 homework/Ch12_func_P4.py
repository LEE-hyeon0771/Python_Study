'''
분해 : 배수, 최댓값, mul(n,max_num)함수, 입력값, 잘못된 입력 인식, for문, if else문
패턴인식 : 배수와 최댓값을 입력받는다.
           문제에서 배수는 n, 최댓값은 max_num으로 변수가 설정되어있음
           mul(n,max_num)함수를 정의한다.
           최댓값이 배수보다 클 경우 최댓값까지의 모든 배수를 출력한다.
           최댓값으로 배수와 같거나 배수보다 작은 숫자가 전달되면 '잘못된 입력입니다.'를 출력한다.
           입력값만 존재한다.
추상화 : 배수와 최댓값을 입력받는다.
         mul(n,max_num)함수를 정의할때 for문을 사용하여 곱해지는 배수를 i로 정해준다.
         만약 곱해지는 배수가 max_num보다 작으면 계속 출력, 아니면 break한다.
         만약 max_num이 n과 같거나 n보다 작으면 잘못된 입력임을 출력한다.
         입력값만 있기 때문에 함수호출 때 =기호 없이 함수만 호출한다.

알고리즘(의사코드)

def mul(n,max_num) :
    for i in range(1~max_num):
        result = n*i
        if result < max_num:
            result를 출력
        else:
            break

        if max_num == n or max_num < n:
            잘못된 입력입니다. 출력

n입력받기
max_num입력받기

mul(n,max_num) 호출
'''
#자동화


def mul(n,max_num) :
    for i in range (1,max_num,1):
        result = n * i
        if result < max_num:
            print(f"{result}")
        else:
            break
        
    if max_num == n or max_num < n:
            print(f"잘못된 입력입니다.")

n = int(input("배수 입력: "))
max_num = int(input("최댓값 입력: "))

mul(n,max_num)
