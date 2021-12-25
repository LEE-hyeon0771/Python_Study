Korean, English, Math, Science = map(int,input().split())

total = Korean + English + Math + Science
avg = total/4

if avg >= 80:
    print("합격")
else:
    print("불합격")
