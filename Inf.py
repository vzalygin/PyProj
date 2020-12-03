def func(n, x, y):
    if n == 1:
        print(n, x, y)
    else:
        func(n-1, x, 6-x-y)
        print(n, x, y)
        func(n-1, 6-x-y, y)


func(int(input()), 1, 3)
