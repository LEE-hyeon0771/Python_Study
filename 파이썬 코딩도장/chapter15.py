Age = int(input())

money = 9000

if 7<=Age<=12:
    money -= 650
elif 13<= Age <= 18:
    money -= 1050
else:
    money -= 1250

print(money)
