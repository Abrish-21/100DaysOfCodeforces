def compareString(m,n):
    m = m.lower()
    n = n.lower()
    if m < n:
        return -1
    elif n  < m:
        return 1
    return 0

m = str(input())
n = str(input())
print(compareString(m,n))