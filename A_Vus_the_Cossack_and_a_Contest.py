def contestAward(m,p,n):
    if (m <=n and m <=p):
        return "Yes"
    return "No"
m,p,n = map(int, input().split())
print(contestAward(m,p,n))
