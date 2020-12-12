def main():
    l = input()
    a = [int(x) for x in input().split()]
    m1 = max(a)
    a.remove(m1)
    m2 = max(a)
    with open('task1_out.txt', 'w') as f:
        f.write(str(m1) + ' ' + str(m2))
        print('result in file task1_out.txt')


main()
