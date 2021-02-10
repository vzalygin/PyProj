def perim(a, b, c):
    return a + b + c


def canBe(a, b, c):
    return a + b > c and a + c > b and c + b > a \
           and a > 0 and b > 0 and c > 0


def main():
    a, b, c = [int(x) for x in input().split()]
    p = 0
    if canBe(a, b, c):
        p = perim(a, b, c)
    with open('task3_out.txt', 'w') as f:
        if p > 0:
            f.write(str(p))
        else:
            f.write("a triangle with such sides doesn't exist")
        print('result in file task3_out.txt')


main()
