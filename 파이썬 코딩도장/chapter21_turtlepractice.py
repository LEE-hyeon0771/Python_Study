import turtle as t

n, length = map(int, input().split())
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.fd(length)
    t.right((360/n) *2)
    t.fd(length)
    t.left(360/n)
