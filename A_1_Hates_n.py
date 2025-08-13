def Hates():
    t = int(input())
    arr = list(map(int, input().split()))
    min_no = min(arr)
    max_no = max(arr)
    diff = 0
    for i in range(len(arr)):
        if( arr[i] == min_no) or (arr[i] == max_no):
            diff = len(arr) - arr.index(arr[i]) - 1
            return diff
2,1,3
print(Hates())



