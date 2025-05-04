def letters():
    m,n = map(int, input().split())

    dorms = list(map(int, input().split()))
    for i in range(1,len(dorms)):
        dorms[i]+= dorms[i-1]
   
    letters = list(map(int, input().split()))

    curr_dorm = 0
    for letter in letters:
        room = letter
        if letter <= dorms[curr_dorm]:
            dorm = curr_dorm + 1
            if curr_dorm >=1:
               room = letter - dorms[curr_dorm -1]
            print(dorm, room)
        else:
            while dorms[curr_dorm] < letter:
                curr_dorm += 1
            
            dorm = curr_dorm + 1
            room = letter - dorms[curr_dorm -1]
            print(dorm, room)



    
letters()