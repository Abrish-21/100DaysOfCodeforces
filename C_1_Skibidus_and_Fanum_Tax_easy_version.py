def arrenge(m):
    for _ in range(m):
        a,b = map(int, input().split())
        arr1 = list(map(int, input().split()))
        arr2 = int(input())
        ans = "YES"
        for i in range(a-1):
            if arr1[i] - arr2 > arr1[i+1] - arr2:
                ans = "NO"
                break
        print(ans)
        ans = "YES"
m = int(input())
arrenge(m)