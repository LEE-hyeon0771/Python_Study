#음수 입력전까지 들어온 점수의 평균 내는 프로그램


total_sum = 0
count = 0

whlie True:
    score = int(input("점수 입력 : "))
    if  score < 0:
          break
    else:
         total_sum  = total_sum + score
         count = count + 1
    

if count == 0:
    print(f"성적의 평균은 0 입니다.")
else :
    aver = total_sum / count
    print(f"성적의 평균은 {aver}입니다.")
