#24.5

para = input().split()

count = 0

for i in para:
    if(i.strip(",.") == "the"):
        count += 1
print(count)


#24.6

money = list(map(int, input().split(";")))

money.sort(reverse = True)

for i in money:
    print('%9s' % format(i,','))
    

