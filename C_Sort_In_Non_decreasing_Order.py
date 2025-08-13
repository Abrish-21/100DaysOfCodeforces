t = int(input())
for _ in range(t):
    def swap():
        m, n = map(int, input().split())
        arr = list(map(int, input().split())) 
        swap_arr = list(map(int,input().split()))
        if arr == sorted(arr):
            return "YES"
        p = set()
        t = set()
        for num in swap_arr:
            if arr[num-1] != arr[num]:
                p.add((num, num+1))
        for i in range(m):
            for j in range(m-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    t.add((j+1, j+2))
        if p == t:
            return "YES"
        else:
            return "NO"
    print(swap())
                