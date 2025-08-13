
t = int(input())
for _ in range(t):
    n = int(input())
    direction = str(input())
    dir = [0,0]
    def Alperen_s():
        for char in direction:
            if char == "U":
                dir[0] += 1
            elif char == "D":
                dir[0] -= 1
            elif char == "R":
                dir[1] += 1
            else:
                dir[1] -=1
            # check for candy 
            if dir == [1,1]:
                return "YES"
        return "NO"
    print(Alperen_s())
                

