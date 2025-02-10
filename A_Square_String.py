def squareString(m):
    for _ in range(m):
        s = str(input())
        if len(s) <= 1 or len(s)%2 != 0:
            print("NO")
        else:
            mid_point  = len(s) // 2 
            if s[:mid_point] == s[mid_point:]:
                print("YES")
            else:
                print("NO")
m = int(input())
squareString(m)
