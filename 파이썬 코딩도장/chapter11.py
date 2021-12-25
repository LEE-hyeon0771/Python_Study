#1

x = input().split()
del x[5:]
print(tuple(x))

#2
x = input()
y = input()

x = x[1::2]
y = y[0::2]
print(x + y)
