def main():
    l = input()
    a = [int(x) for x in input().split()]
    n_min = min(a)
    n_max = max(a)
    for i in range(len(a)):
        if a[i] == n_min:
            a[i] = n_max
    with open('task2_out.txt', 'w') as f:
        s = ''
        for n in a: s += str(n) + ' '
        f.write(s)
        print('result in file task2_out.txt')


main()
