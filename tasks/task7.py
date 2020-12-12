def maks(x, y):
    if x >= y: return x
    else: return y


def main():
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    z = maks(a, 2*b)*maks(2*a - b, b)
    with open('task7_out.txt', 'w') as f:
        f.write(str(z))
        print('result in file task7_out.txt')


main()
