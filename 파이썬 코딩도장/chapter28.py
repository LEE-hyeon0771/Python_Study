with open('word.txt','r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if(word == word[::-1]):
                print(word.strip('\n'))
