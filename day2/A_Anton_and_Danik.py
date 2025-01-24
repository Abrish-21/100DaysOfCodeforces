def whoWon(n,score):
    anton_count = 0
    danik_count = 0
    result = ''
    for i in score:
        if i =="A":
            anton_count +=1
        else:
            danik_count +=1
    if anton_count > danik_count:
        result = "Anton"
    elif danik_count > anton_count:
        result = "Danik"
    else:
        result = "Friendship"
    return result
# Problem: First line is the number of games, second line is the scores.
n = int(input())  # Read the number of games
score = input()   # Read the string of scores
print(whoWon(n,score))

