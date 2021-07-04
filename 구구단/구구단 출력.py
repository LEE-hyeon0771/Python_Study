
#구구단 출력

dan = int(input("출력할 단을 입력하시오: "))
for i in range(1,10,1):
    print(f"{dan}*{i} = {dan*i:2d}")


#return이 없고 인수가 있는 경우
def multi(dan):
    for i in range(1, 10):
         print(f'{dan} * {i} = {dan*i:2d}')

dan = int(input("단을 입력하시오 : "))

multi(dan)

#return이 있고 인수가 있는 경우

def multi(dan):
    
    for i in range(1, 10):
        result = dan * i
        print(f"{dan} * {i} = {result}")
    return result
        
dan = int(input("단을 입력하시오 : "))
result = multi(dan)


#return이 없고 인수가 없는 경우

def multi():
    dan = int(input("단을 입력하시오 : "))
    for i in range(1, 10):
         print(f'{dan} * {i} = {dan*i:2d}')

multi()

#return이 있고 인수가 없는 경우

def multi():
    dan = int(input("단을 입력하시오 : "))
    for i in range(1, 10):
        result = dan * i
        print(f"{dan} * {i} = {result}")
    return result
        

result = multi()
