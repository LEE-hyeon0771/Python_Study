keys = input().split()
values = map(int, input().split())

x=dict(zip(keys,values))
del x['delta']       #key 값은 del로 삭제
x = {key: value for key, value in x.items() if value != 30}        #value 값은 딕셔너리 표현식으로 삭제

print(x)
