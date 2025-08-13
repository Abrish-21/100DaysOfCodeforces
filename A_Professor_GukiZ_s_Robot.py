
def robot():
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())
    result = max(abs(x2-x1), abs(y2-y1))
    print(result)
robot()