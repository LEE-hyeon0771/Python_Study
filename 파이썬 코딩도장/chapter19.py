n = int(input())

for i in range(n):
    for j in reversed(range(n)):   #reversed로 오른쪽에 붙은 직각삼각형 그림
        if i < j:
            print(" ",end=" ")
        else:
            print("*",end = " ")
    for j in range(n):          #그냥 이중 for문으로 왼쪽에 붙은 직각삼각형 그림
        if i > j:
            print("*",end=" ")
    print()
            
