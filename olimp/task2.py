def func(x, y):
    if (y % 2 == 0 and x % 2 == 1) or (y % 2 == 1 and x % 2 == 0):
        print(-1)
        exit()
    if x > 0 and y > 0 and x / y == 1:
        print(0)
        exit()
    k = abs(x - y) // 2
    if x > 0 and y > 0:
        print(1)
        if abs(x) > abs(y):
            x1 = x - k
            y1 = y + k
            print(x1, y1, 'H')
        else:
            x1 = x + k
            y1 = y - k
            print(x1, y1, 'W')
    elif x < 0 and y > 0:
        print(2)
        print(1, 1, 'W')
        k = -abs(x-y)//2
        print(k)
        if abs(y) < abs(x):
            x1 = x - k
            y1 = y - k
            print(x1, y1, 'H')
        else:
            x1 = -x + k
            y1 = y - k
            print(x1, y1, 'H')
    elif x > 0 and y < 0:
        print(2)
        print(1, 1, 'H')
    else:
        print(3)


func(-1, 5)
print('=======')
func(-5, 1)
