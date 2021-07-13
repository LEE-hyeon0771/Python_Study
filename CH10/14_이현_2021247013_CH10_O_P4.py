'''
분해 : 자동판매기, 100원짜리 지폐, 500원짜리 동전, 100원짜리 동전, 거스름돈
       10원짜리, 1원짜리 거스름돈 용 동전
패턴인식 : 물건값을 입력하면 1000원, 500원, 100원 으로 물건값을 계산한다.
           동전의 개수를 입력하면 거스름돈을 계산하여 동전으로 반환한다.
           거스름돈은 500원,100원,10원,1원짜리로만 이루어진다.
추상화 : input을 사용하여 물건값,1000원 지폐 개수, 500원,100원 동전 개수를 입력받는다.
         물건값과 지폐, 동전이 정수이므로 int를 사용하여 강제형 변환을 시켜준다.
         거스름돈 = 지불할돈 - 물건값으로 선언해준다.
         거스름돈은 나머지로 계산하여 선언해준다.
         f-string 방식을 사용하여 거스름돈을 print 해준다.
'''

price = int(input("물건값을 입력하시오: "))
paper1000 = int(input("1000원 지폐개수: "))
coin500 = int(input("500원 동전개수: "))
coin100 = int(input("100원 동전개수: "))

change = (paper1000*1000 + coin500*500 + coin100*100) - price

numcoin500 = change//500
change = change%500

numcoin100 = change//100
change = change%100

numcoin10 = change//10
change = change%10

numcoin1 = change//1
change = change%1

print(f"거스름돈: 500원={numcoin500} 100원={numcoin100} 10원={numcoin10} 1원={numcoin1}")



