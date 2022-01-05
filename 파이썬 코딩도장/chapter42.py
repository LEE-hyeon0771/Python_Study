def html_tag(x):
    def real_decorator(func):
        def wrapper():
            r = func()
            return '<{0}>{1}</{2}>'.format(x,r,x) #return 으로 해 줘야만 @가 겹쳐서 이중으로 들어가짐.
        #print로 하고 return r 하면 따로 따로 반영이 되어서 나옴.
            
        return wrapper
    return real_decorator




a,b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'

print(hello())
