def main():
    n = input()
    if len(n) % 2 == 0:
        n1, n2 = n[:len(n)//2], n[len(n)//2:]
    else:
        n1, n2 = n[:len(n)//2+1], n[len(n)//2:]
    s1, s2 = sum([int(x) for x in n1]), sum([int(x) for x in n2])
    with open('task9_out.txt', 'w') as f:
        f.write(str(s1) + ' ' + str(s2))
        print('result in file task9_out.txt')


main()
