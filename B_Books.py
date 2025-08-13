from collections import defaultdict


m,n = map(int, input().split())
arr = list(map(int, input().split()))
longest_p = 0
curr_sum  = 0
start = 0
for end in range(m):
    curr_sum += arr[end]
    while curr_sum > n:
        curr_sum -= arr[start]
        start += 1
    longest_p = max(longest_p, end - start + 1)
print(longest_p)




