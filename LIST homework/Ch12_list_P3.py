'''
분해 : 1~100까지의 짝수, 리스트, range

패턴인식 : 1~100까지의 짝수들을 리스트의 원소로 한다.

추상화 : 1~100까지의 짝수를 range(2,101,2)로 표현한다.
         range는 list가 아니므로 list로 바꾸어 표현해 주어야한다.
         list를 출력한다.

알고리즘(의사코드)

짝수 -> range(2,101,2)

range를 리스트로 바꾸어 표현

1~100까지의 짝수 리스트 출력
'''
#자동화


even_range = range(2,101,2)

even_list = list(even_range)

print(f"{even_list}")
