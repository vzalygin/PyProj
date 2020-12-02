def euclidean(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


def main():
    a, b, c = [int(x) for x in ((((input().replace(' ', '')).replace('x', ' ')).replace('y', ' ')).replace('+', ' ')).replace('=', ' ').split()]
    print(a, b, c, '')
    print(euclidean(a, b))
    if c % euclidean(a, b) != 0:
        print('No solution')
        exit()


main()
