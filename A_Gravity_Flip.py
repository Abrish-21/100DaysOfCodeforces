def gravityFilp(m,arr):
    arr.sort()
    return ' '.join(map(str, arr))
m = int(input())
arr = list(map(int, input().split()))
print(gravityFilp(m,arr))
