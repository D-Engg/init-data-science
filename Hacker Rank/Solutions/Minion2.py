#Minion Game

def minion_game(sample_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    stuart, kevin = 0, 0
    for i in range(len(sample_string)):
        temp = ''
        for j in range(i, len(sample_string)):
            temp += sample_string[j]
            if temp[0] in vowels:
                kevin += 1
            else:
                stuart += 1
    if stuart > kevin:
        print('Stuart {}'.format(stuart))
    else:
        print('Kevin {}'.format(kevin))

sample_string = input()
minion_game(sample_string)
