def check():
    word = str(input())

    check = {"H", "Q", "9","+"}
    for char in word:
        if char in check:
            return "YES"
    return "NO"
print(check())