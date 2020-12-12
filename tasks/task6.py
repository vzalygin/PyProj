def func(n):
    n = str(n)
    n_mul = 1
    for c in n: n_mul *= int(c)
    n = n[-1] + n[1:-1] + n[0]
    return int(n), n_mul


def main():
    n = int(input())
    res = func(n)
    with open('task6_out.txt', 'w') as f:
        f.write(str(res[0]) + ' ' + str(res[1]))
        print('result in file task6_out.txt')


main()
