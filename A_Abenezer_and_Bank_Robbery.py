def AbeniRobbery():
    a,b,c = map(int,input().split())
    n = int(input())
    result = 0
    notes = list(map(int, input().split()))
    for x in notes:
        if b < x < c:
            result += 1
    print(result)
    
AbeniRobbery()

