def main():
    n = input()
    min_n = min([x for x in n])
    res = 0
    for c in n:
        if c == min_n: res += 1
    with open('task8_out.txt', 'w') as f:
        f.write(str(res))
        print('result in task8_out.txt')


main()
