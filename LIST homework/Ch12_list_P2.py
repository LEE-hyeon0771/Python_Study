'''
분해 : lang1과 lang2 리스트, 리스트의 원소들

패턴인식 : lang1과 lang2 리스트가 있다.
           lang1리스트 뒤에 lang2 리스트를 붙인 새로운 리스트 langs 생성함

추상화 : lang1 리스트를 선언한다.
         lang2 리스트를 선언한다.
         lang1+lang2를 하면 lang1뒤에 lang2가 그대로 붙는 것을 활용하여
         langs 리스트를 붙인다.

알고리즘 : 의사코드
'''
# 자동화

lang1 = ['C', 'C++', 'JAVA']
lang2 = ['python', 'Go', 'C#']

langs = lang1+lang2

print(f"lang1: {lang1}")
print(f"lang2: {lang2}")
print(f"langs: {langs}")
          
