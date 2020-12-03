def func(n, x, y):
    if n == 1:
        if (y-x) % 3 == 2:  # идём назад или идём вперёд через шаг
            print(n, x, 6-y-x)
            print(n, 6-y-x, y)
        else:
            print(n, x, y)
    else:
        func(n - 1, x, 6 - x - y)
        if (y-x) % 3 != 2:
            print(n, x, y)
            func(n - 1, 6 - x - y, y)
        else:
            func(n-1, 6-x-y, y)
            print(n, x, 6-x-y)
            func(n-1, y, x)
            print(n, 6-x-y, y)
            func(n-1, x, y)


func(int(input()), 1, 3)
