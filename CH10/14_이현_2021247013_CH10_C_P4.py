'''
분해 : 두 개의 정수, 둘 중 큰 수
패턴인식 : 두 개의 정수를 입력 받는다.
           둘 중 큰수를 구별 한다.
추상화 : input을 사용하여 첫번째 정수, 두번째 정수를 입력받는다.
         두 정수 모두 정수이므로 int로 강제형 변환을 시켜준다.
         if else 문을 사용 하여 둘 중 큰 수를 구별 한다.
         구별한 큰 수를 print 한다.
'''
#알고리즘

first_int = int(input("첫 번째 정수: "))
second_int = int(input("두 번째 정수: "))

if first_int > second_int :
    print(f"큰 수는 {first_int}")
else :
    print(f"큰 수는 {second_int}")
