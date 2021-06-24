'''
분해 : 두개의 정수, 더 큰 수 찾기, get_max()함수, 입력값, 반환값, max내장함수
패턴인식 : 두개의 정수를 입력받는다.
           두 정수 중 더 큰 수를 찾는다.
           get_max()함수를 사용한다.
           입력값과 반환값이 모두 존재해야 한다.
추상화 : get_max(첫번째수, 두번째수)로 정의하고 더 큰 수를 max함수를 사용하여 반환한다.
         첫번째 수와 두번째 수를 int와 input을 사용하여 입력받는다.
         반환값이 있으므로 result = 함수호출의 형태로 호출한다.
알고리즘(의사코드)

def get_max(첫번째수, 두번째수):
    return max(첫번째수, 두번째수)

첫번째 수 입력받기
두번째 수 입력받기

result = get_max(첫번째수, 두번째수)

{result} 출력

'''
#자동화

def get_max(first,second) :
    return max(first,second)

first = int(input("첫 번째 정수를 입력하시오: "))
second = int(input("두 번째 정수를 입력하시오: "))

result = get_max(first,second)

print(f"큰 수는 {result}")
 
