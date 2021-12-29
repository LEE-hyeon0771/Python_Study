x,y = map(int, input().split())

a= {i for i in range(1,x+1) if x%i == 0}
b= {i for i in range(1,y+1) if y%i == 0}

divisor = a&b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
