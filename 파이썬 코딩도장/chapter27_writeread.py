lines = ['안녕하세요.\n', '파이썬\n','코딩 도장입니다.\n']

with open('hello world.txt','w') as file:
    file.writelines(lines)

with open('hello world.txt','r') as file:
    lines = file.readlines()
    print(lines)

with open('hello world.txt','r') as file:
    for line in file:
        print(line.strip('\n'))

'''with open('hello world.txt','r') as file:
    line = None
    while line != ' ':
        line = file.readline()
        print(line.strip('\n'))'''

import pickle

name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean' : 90, 'english' : 95, 'math' : 85, 'science' : 82}

with open('james.p','wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

with open('james.p','rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)

    print(name, age, address, scores, sep='\n')
