def prime_number_generator(start, stop):
    for x in range(start, stop):
        isPrime = True
        for i in range(2, x-1):
            if x%i ==0:
                isPrime = False
        if isPrime == True:
                yield x

start, stop = map(int, input().split())

g = prime_number_generator(start, stop)
print(type(g))

for i in g:
    print(i, end=' ')
