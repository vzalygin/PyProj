def func(a, c, shift):
    i, j = c[0]+shift[0], c[1]+shift[1]
    while 0 <= i < 8 and 0 <= j < 8:
        for e in a:
            if i == e[0] and j == e[1]:
                return True
        i, j = i+shift[0], j+shift[1]
    return False


def main():
    f = []
    for _ in range(8):
        y, x = input().split()
        f.append((int(y)-1, int(x)-1))
    intersection = False
    for e in f:
        shifts = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
        for s in shifts:
            intersection = intersection or func(f, e, s)
    if intersection:
        print('YES')
    else:
        print('NO')


main()
