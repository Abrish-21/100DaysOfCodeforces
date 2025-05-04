def AbeniString():
    t = int(input())
    for _ in range(t):
        m= int(input())
        word = str(input())
        word_l = [letter for letter in word]
        # print(word_l)
        min_chr =  min(word_l)
        max_chr = max(word_l)
        print(ord(max_chr) - 96)
AbeniString()
        