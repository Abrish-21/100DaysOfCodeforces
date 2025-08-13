t = int(input())
for _ in range(t):
    num = int(input())
    y = 0
    while not (num & y > 0) and (num ^ y > 0):
        y += 1
    print(y)

