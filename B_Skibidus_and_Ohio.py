def minString(m):
    for _ in range(m):
        word = str(input())
        size = len(word)
        min_word = False
        if len(word) == 1:
            print(1)
        else:
            for i in range(1,size):
                if word[i] == word[i-1]:
                    min_word = True
        if min_word == True:
            print(1)
        else:
            print(size)
m = int(input())
(minString(m))