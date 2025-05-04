def Cards():
    t = int(input())
    nums = list(map(int, input().split()))
    sorted_num = sorted(nums)

    left = 0
    right = len(sorted_num) -1
    while left < right:
        x = nums.index(sorted_num[left]) +1
        nums[nums.index(sorted_num[left])] = -1
        y = nums.index(sorted_num[right])+1
        nums[nums.index(sorted_num[right])] = -1
        print(x,y)

        left += 1
        right -=1
        


Cards()