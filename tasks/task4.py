def main():
    m = int(input())
    s = ''
    for n in range(m):
        for _ in range(n+1):
            s += '*'
        s += '\n'
    with open('task4_out.txt', 'w') as f:
        f.write(s)
        print('result in file task4_out.txt')


main()
