start, stop = map(int, input().split())

def wrong():
    if start < 1 or start>20:
        print("start값을 잘못입력하셨습니다.")
    elif stop < 10 or stop > 30:
        print("stop값을 잘못입력하셨습니다.")
    elif start >= stop :
        print("start값 보다 stop값을 크게 입력해주십시요.")
        


if 1<= start <= 20 and 10 <= stop <= 30 and start < stop:
    printlist = [2**i for i in range(start,stop+1)]
    del printlist[1]
    del printlist[-2]
    print(printlist)
else:
    wrong()
