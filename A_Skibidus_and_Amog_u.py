def toPlural():
    m = int(input())

    for _ in range(m):
        string  = str(input())
        if string == '':
            print("i")
        else:
            size = len(string)
            arr = [i for i in string]
            arr = arr[:size-2]
            arr.append("i")
            print( ''.join(arr))
toPlural()