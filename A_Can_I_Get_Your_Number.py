def getNumber():
    number = []
    answer = 0
    t = int(input())
    for _ in range(t):
        number.append(str(input()))
    for i in range(len(number[0])):
        for j in range(len(number)-1):
            if number[j][i] != number[j+1][i]:
                return answer
        answer += 1



print(getNumber())
