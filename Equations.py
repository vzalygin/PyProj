def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# a   m  c
# 3y =3= 0    a = 3
# -2y =3= 2   b = -2   a = -2
# 1y =3= 2             b = 1  a = 1
# 0y =3= 4                    b = 0
# y = 3*f+2
def finding_solution_second_var(b, m, c):
    a = m
    prev_c = c
    while b != 0:
        d = (a // -b)
        prev_c = c
        c *= d
        a, b = b, a + b * d
        print((str(b) + 'y =' + str(m) + '= ' + str(c)))
    if a < 0:
        prev_c = -prev_c
    return prev_c


# 6x - 10y = 4
def main():
    # a, b, c = int(input()), int(input()), int(input())
    a, b, c = 6, -10, 4
    e = abs(euclidean(a, b))
    if c % e == 0:
        print(str(a) + 'x + ' + str(b) + 'y = ' + str(c))
        a //= e
        b //= e
        c //= e
        d = 0
        m = 0
        if a < b:
            m = b
            if a > 0: a %= b
            else: a %= -b
            if c > 0: c %= b
            else: c %= -b
            d = finding_solution_second_var(a, m, c)
            print('x = ' + str(b) + 'i + ' + str(d))
            # print(str(a) + '(' + str(b) + 'i + ' + str(d) + ') + ' + str(b) + 'y = ' + str(c))
        else:
            m = a
            if b > 0: b %= a
            else: b %= -a
            if c > 0: c %= a
            else: c %= -a
            d = finding_solution_second_var(b, m, c)
            print('y = ' + str(a) + 'i + ' + str(d))
            # print(str(a) + 'x + ' + str(b) + '(' + str(a) + 'i + ' + str(d) + ') = ' + str(c))
    else:
        print('no solution')


main()
