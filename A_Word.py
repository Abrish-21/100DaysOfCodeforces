def uniformCase(word):
    lower_c = 0
    upper_c  = 0
    for char in word:
        if ord(char) >= 95:
            lower_c +=1
        else:
            upper_c +=1
    if lower_c > upper_c:
        return word.lower()
    elif upper_c > lower_c:
        return word.upper()
    return word.lower()
word = str(input())
print(uniformCase(word))
