def reduceImp():
    t = int(input())
    for _ in range(t):
        n = int(input())
        word = list(map(str, input().split()))
        result = ["0"]* n
        for i in range(1,n):
            if i >0 and word[i-1] == "?":
                if word[i] == "R":
                    word[i-1] = "B"
                else:
                    word[i-1] = "R"
        
        print (' '.join(map(str,result)))
reduceImp()

