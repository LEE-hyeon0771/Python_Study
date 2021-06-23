'''
분해 : 방번호, 0~9번까지의 수, 최소값, 6과 9의 교차 가능, str강제형변환, count 메소드,
       max내장함수, 리스트

패턴인식 : 방 번호를 0~9까지의 수 네자리로 입력받는다.
           6과 9는 서로 교차가 가능하다.
           필요한 세트의 개수의 최소값을 구한다.

추상화 : 방번호를 input으로 입력받는다.
         필요한 세트 번호를 리스트화 한다.
         방 번호에 9가 들어가면 6으로 바꾼다.
         필요한 세트 번호의 리스트를 count메소드로 세어준다.
         리스트의 값을 str로 처리한다.
         6과 9를 제외한 수 중 가장 많이 나온 수가 필요한 세트 수
         6과 9를 더해 하나로 생각한 수가 2로 나누어 나머지가 없다면 몫이 필요한 세트수
         6과 9를 더해 하나로 생각한 수가 2로 나누어 떨어지지 않는다면 몫에 +1을 해주어야 함
         6과 9를 만드는데 필요한 개수와 6과 9가 아닌 수에 필요한 개수를 비교하여 커야함.

알고리즘(의사코드)

방 번호 입력받기

세트 수 리스트 만들기

6과 9를 담을 변수 except_num 초기화
(except_num = 0)

0~9 사이의 수들의 개수를 구함(반복문 for 이용)
구하는 중에 6과 9일 경우 수를 따로 구함(except_num에 넣어줌)

-> for i in range(10) :
     세트 리스트 = 방번호.count(str(i))
     if i == 6 or i==9 :
     세트 리스트 = 0
     except_num = except_num + 방번호.count(str(i))

6과 9를 하나로 생각

if except_num % 2 == 0 :
   except_num = except_num // 2

else :
   except_num = except_num // 2 + 1

max 함수를 사용하여 큰 쪽을 출력

'''

#자동화


room_number = input("방 번호 입력: ")

set_number = [0,1,2,3,4,5,6,7,8,9]

except_num = 0

for i in range(10):
   set_number[i] = room_number.count(str(i))
   if i == 6 or i == 9:
      set_number[i] = 0
      except_num = except_num + room_number.count(str(i))


if except_num % 2 == 0:
   except_num = except_num // 2
else:
   except_num = except_num //2 + 1

max_num = max(except_num,max(set_number))
print(f"{max_num}")    


