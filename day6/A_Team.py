def acceptedSol(m):
    accepted_sol = 0
    
    for _ in range(m):
        arr = list(map(int, input().split()))
        one = arr.count(1)
        zero = arr.count(0)
        if one > 1:
            accepted_sol +=1
    return accepted_sol
m = int(input())
print(acceptedSol(m))



