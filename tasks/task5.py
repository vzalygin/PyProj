def array_sum(a):
    s = 0
    for n in a: s += n
    return s


def main():
    a = [int(x) for x in input().split()]
    s = array_sum(a)
    with open('task5_out.txt', 'w') as f:
        f.write(str(s))
        print('result in file task5_out.txt')


main()
