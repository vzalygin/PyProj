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


print(func(7, 29, 1))