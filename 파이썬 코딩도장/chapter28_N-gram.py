# 공백 단위로 자른 문자열의 2-gram
text = 'this is python script'
words = text.split()

for i in range(len(words) - 1):
    print(words[i], words[i+1])


# zip 함수로 2-gram 만들기
text1 = 'hello'

two_gram = zip(text1, text1[1:])     #zip을 이용하여 반복 가능한 객체의 각 요소를 튜플로 만듦
for i in two_gram:
    print(i[0],i[1],sep=' ')

split_twogram = list(zip(words,words[1:]))
for j in split_twogram:
    print(j[0],j[1],sep=' ')
          
