def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def func(a, m, c):
    a %= m
    c %= m
    b = a
    a = m
    c0 = 0
    while b != 0:
        k = -(a // b)  # на сколько надо умножить b
        a, b = b, a % b
        c0, c = c, c0 + c * k
    if c0 % m < abs(c0): c0 = c0 % m
    return m, c0


def main():
    a, b, c = [int(i) for i in input().split()]
    e = euclidean(a, b)
    if a == 0 and b == 0:
        if c == 0:
            print('y = 1j')
            print('x = 1k')
        else:
            print('No solution')
        exit()
    elif a == 0:
        if c % b == 0:
            c //= b
            print('y = ' + str(c))
            print('x = 1j')
        else:
            print('No solution')
        exit()
    elif b == 0:
        if c % a == 0:
            c //= a
            print('y = 1j')
            print('x = ' + str(c))
        else:
            print('No solution')
        exit()
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
    m *= b
    c0 *= b
    c -= c0
    c //= a
    m = -m
    m //= a
    print('x = ' + str(m) + 'k + ' + str(c))


main()
