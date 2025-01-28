def identifyGender(arr):
    store_char = set()
    for  i in arr:
        store_char.add(i)
    if len(store_char)%2 ==0:
        return "CHAT WITH HER!"
    return "IGNORE HIM!"
arr = str(input())
print(identifyGender(arr))