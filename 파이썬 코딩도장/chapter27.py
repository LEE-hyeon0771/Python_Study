with open('words.txt.','r') as file:
    for line in file:
        string = line.split()
        for word in string:
            if 'c' in word:
                print(word.strip(',.'))
