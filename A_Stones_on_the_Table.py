def pickStone(m,arr):
    if m <=1:
        return m
    else:
        count  = 0
        for i in range(m-1):
            if (arr[i] == arr[i+1]):
                count +=1
        return count
m = int(input())
arr = str(input())
print(pickStone(m,arr))
    


