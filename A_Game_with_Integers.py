def game():
    move = 1
    n = int(input())

    while move <= n:
        m = int(input())
        if move > 10:
            print("Second")
        if (m - 1) % 3 == 0 or (m + 1) % 3 == 0:
            print("First")
        else:
            print("Second")

        move += 1 


game()
