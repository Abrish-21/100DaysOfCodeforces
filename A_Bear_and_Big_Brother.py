import math
def whoIsBig(a,b):
    val = math.log((b/a), 3/2)
    if (val == int(val)):
        return int(val) + 1
    return math.ceil(val)
a,b = map(int, input().split())
print(whoIsBig(a,b))