def beautifulMatrix():
    row = 5
    col = 5
    min_moves = 0
    for i in range(5):
        arr = list(map(int, input().split()))
        if (1 in arr):
            current_loc = arr.index(1) + 1
            min_moves = abs(current_loc - 3) +  abs(i-3 + 1) 
    return min_moves
print(beautifulMatrix())


