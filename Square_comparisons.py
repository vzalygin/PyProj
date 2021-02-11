import random


def solvability(a, p):
    return a ** ((p - 1) // 2) % p == 1


def is_simple(p):
    return ((p - 3) / 4).is_integer()


def simple_solution(a, p):
    g = abs(a ** ((p + 1) // 4) % p)
    return g, -g


def k_search(a, p):
    k = 0
    while a % p != p - 1:
        a **= 2
        k += 1
    return k


def sq_search(p):
    p -= 1
    s = 0
    q = p / (2 ** s)
    while q % 2 != 1:
        s += 1
        q = p / (2 ** s)
    return s, int(q)


def squaring(b, k):
    for _ in range(k):
        b **= 2
    return b


def b_search(p, k):
    s, q = sq_search(p)
    n = random.randrange(1, p)  # поиск невычета
    while solvability(n, p):
        n = random.randrange(1, p)
    print(f'{n} является невычетом')
    b = (n ** q)
    while squaring(b, k + 1) % p != p - 1:
        b **= 2
    return b


# проверка на решимость
# проверка на простую ситуацию (и решение в лучшем случае)
# определение q, x_0 и проверка, является ли x_0 решением
def main():
    a = 8
    p = 17
    if not solvability(a, p):
        print(f'{a} является невычетом')
        print('нет решений')
        exit()
    if is_simple(p):
        print('простая ситуация')
        print('x=', simple_solution(a, p))
        exit()
    print('сложная ситуация')
    s, q = sq_search(p)
    print(f's={s}, q={q}')
    x = a ** ((q + 1) // 2) % p
    t = a ** q
    # if t % p == 1:
    #     print('x_0 является ответом. x_0 =', (x, -x))
    #     exit()
    # print(f'x_0({x}) не является ответом')
    # k = k_search(t, p)
    # b = b_search(p, k)
    # print('k:', b, 'b:', b)
    # x *= b
    # t *= b ** 2
    # if t % p == 1:
    #     print('x_1 является ответом. x_1 =', ((x % p), -(x % p)))
    #     exit()
    counter = 0
    while True:
        if t % p == 1:
            print(f'x_{counter} является ответом. x_{counter} =', ((x % p), -(x % p)))
            exit()
        print(f'x_{counter}({x}) не является ответом')
        counter += 1
        k = k_search(t, p)
        b = b_search(p, k)
        print('k:', b, 'b:', b)
        x *= b
        t *= b ** 2


main()
