'''file = open('hello world.txt','w')
file.write('Hello, world!')
file.close()

file = open('hello world.txt','r')
s = file.read()
print(s)
file.close()'''

with open('hello world.txt','r') as file:
    s= file.read()
    print(s)
# with as 로 파일을 열게 될 경우 close를 안시켜줘도 됨
