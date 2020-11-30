def move(n, x, y):
    if n == 1:
        print(n, 1, 3)
    else:
        dop = 6-3-1
        move(n-1, 1, 2)
        print(n-1, 1, 3)
        move(n-1, 2, 3)

move(int(input()), 1, 3)
