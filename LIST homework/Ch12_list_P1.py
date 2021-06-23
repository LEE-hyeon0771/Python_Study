'''
분해 : 비어있는 리스트, 5개의 정수 입력 받기, 리스트 내용, 평균 계산, sum 메소드
       개수 변수(count), append 메소드, 반복문(while)사용

패턴인식 : 5개의 정수를 입력받는다.
           리스트의 합과 평균을 구한다.
           입력 받은 리스트의 값들을 출력한다.

추상화 : 빈 리스트를 만든다.
         count = 0 으로 초기값을 설정한다.
         반복문 while을 사용한다.
         5개의 정수를 int와 input을 사용하여 입력받아 비어 있는 리스트에 저장한다.
         append 메소드를 활용하여 빈 리스트에 입력받은 리스트를 저장한다.
         sum 메소드를 사용하여 리스트의 값을 더한다.
         리스트 값들의 합을 개수로 나누어 평균을 구한다.

알고리즘(의사코드)

빈 리스트 생성
count = 0 으로 설정

while count<5 : 
     값 5개 입력받기
     count = count+1
     빈 리스트에 append메소드로 입력받은 값 5개를 저장

평균 = 리스트 합/개수

리스트와 평균 출력

'''
# 자동화
val_list = []
count = 0
while count < 5 :
    input_val = int(input("Enter 5 integers: "))
    count = count + 1
    val_list.append(input_val)


avg_list = sum(val_list)/len(val_list)

print(f"{val_list}")
print(f"평균: {avg_list}")
               


