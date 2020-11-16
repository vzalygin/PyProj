def phib(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return phib(n-1)+phib(n-2)


print(phib(int(input())-1))
