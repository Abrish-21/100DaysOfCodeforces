def cardGame(m,arr):
    left = 0
    right  = m -1
    score1 = 0
    score2  = 0
    while left <= right :
        # serje's turn
        if arr[left] > arr[right]:
            score1 += arr[left]
            left +=1
        elif arr[right] > arr[left]:
            score1 += arr[right]
            right -= 1
        else:
            score1 += arr[left]
            left +=1
        if left <= right:
            # Dima's turn
            if arr[left] > arr[right]:
                score2 += arr[left]
                left +=1
            elif arr[right] > arr[left] :
                score2 += arr[right]
                right -=1
            else:
                score2+= arr[left]
                left +=1
    result = [score1,score2]
    return ' '.join(map(str, result))
m = int(input())
arr = list(map(int, input().split()))
print(cardGame(m,arr))
        

 