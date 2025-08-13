def Slim():
    n = int(input())
    slim_row = [1]
    for i in range(1,n):
        slim_row.append(1)
        while len(slim_row) > 1 and slim_row[-1] == slim_row[-2]:
            val = slim_row[-1]
            slim_row.pop()
            slim_row.pop()
            slim_row.append(val + 1)
    print(' '.join(map(str, slim_row)))
Slim()