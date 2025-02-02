def min_pay():
    m = int(input())
    for _ in range(m):
        arr = list(map(int, input().split()))
        a = arr[0]
        b = arr[1]
        if a == 0 and b == 0:
            print(1)
        elif a == 0 and b!=0:
            print(1)
        else:
            print(((a + b*2)+ 1))
min_pay()

