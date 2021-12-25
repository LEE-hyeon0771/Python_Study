start, stop = map(int, input().split())

i= start

while True:
    if start <= i <= stop:
        if i % 10 == 3:
            i+=1
            continue
        print(i, end = " ")
        i+=1
