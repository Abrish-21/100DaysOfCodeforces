def exchange():
    n = int(input())
    for _ in range(n):
        m = int(input())
        nums = list(map(int, input().split()))
        count  = 0
        visited  = set()
        def dfs(n):
        
            nonlocal count
            count  += 1
            result = 0


            while result!= n:
                result = 
                dfs(nums[n-1])
            return result
        ans  = []
        for n in nums:
            result = 
            ans.append(dfs(n))
        print(*ans)
    # ans print(exchange)
        
exchange()