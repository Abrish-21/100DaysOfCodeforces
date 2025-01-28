import math

def BiggerWeight(a,b):
    year = 0
    return  math.ceil(3*a / 2*b)
a,b  = map(int, input().split())
print(BiggerWeight(a,b))