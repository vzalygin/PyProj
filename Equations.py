def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def func(a, m, c):
    # print(str(a) + 'j =' + str(m) + '= ' + str(c))
    a %= m
    c %= m
    b = a
    a = m
    c0 = 0
    # print('==================')
    # print(str(a) + 'y =' + str(m) + '= ' + str(c0))
    # print(str(b) + 'y =' + str(m) + '= ' + str(c))
    while b != 0:
        k = -(a // b)  # на сколько надо умножить b
        a, b = b, a % b
        c0, c = c, c0 + c * k
        # print(str(b) + 'y =' + str(m) + '= ' + str(c))
    if c0 % m < abs(c0): c0 = c0 % m
    return m, c0


def main():
    # a, b, c = [int(x) for x in ((((input().replace(' ', '')).replace('x', ' ')).replace('y', ' ')).replace('+', ' ')).replace('=', ' ').split()]
    # print(a, b, c)
    a, b, c = [int(i) for i in input().split()]
    e = euclidean(a, b)
    if c % e != 0:
        print('No solution')
        exit()
    else:
        print('Solutions are exist')
    a //= e
    b //= e
    c //= e
    m, c0 = func(b, a, c)
    print('y = ' + str(m) + 'k + ' + str(c0))
    # print(str(a) + 'x + ' + str(b) + '*(' + str(m) + 'f + (' + str(c0) + ')) = ' + str(c))
    m *= b
    c0 *= b
    # print(str(a) + 'x + ' + str(m) + 'f + ' + str(c0) + ' = ' + str(c))
    c -= c0
    c //= a
    m = -m
    m //= a
    print('x = ' + str(m) + 'k + ' + str(c))


main()
