import random


print(f"로또의 세계에 오신것을 환영합니다.")
print(f"저희 어플은 begin이라고 적으시면 자동으로 높은 확률의 대박 번호가 뽑힙니다.")
begin = str(input("begin을 적고 시작해보아요!!: "))
num = random.sample(range(1,46),6)        #로또 번호 6개 뽑기
num.sort()


while True:                             #보너스 번호 뽑기(이미 뽑은 로또 번호 6개를 제외한 수 여야함)
    bonus = random.randrange(1,46)      #while문 속에 if문을 걸어줌
    if not bonus in num:
        num.append(bonus)
        break
    
print(f"보너스 번호는 {bonus}입니다.")
print(f"6자리 번호와 보너스 번호는 {num} 입니다.")

print(f"이제 당첨번호를 한번 볼까요 두구두구두구.")
win = str(input("result를 적고 결과를 볼까요!!: "))

result_num = random.sample(range(1,46),6)        #당첨 번호 뽑기


print(f"당첨번호는 {result_num}입니다.")

count = 0
bonus_count = 0
for i in range(0,len(result_num)):                #당첨번호와 보너스 번호 비교
    if result_num[i] == bonus:
        bonus_count = bonus_count + 1
    for j in range(0,len(num)):                   #당첨번호와 본 번호 비교
        if result_num[i] == num[j]:
            count = count + 1

print(f"번호가 {count}개 일치합니다. 보너스 번호는 {bonus_count}개 일치합니다.")

if count == 6:                                 #결과 출력
    print(f"1등입니다.")
elif count == 5 and bouns_count == 1:
    print(f"2등입니다.")
elif count == 5:
    print(f"3등입니다.")
elif count == 4:
    print(f"4등입니다.")
elif count == 3:
    print(f"5등입니다.")
else:
    print(f"다시 한 번 도전해보자구요. 대박쳐야죠!!")














