def to_sys(a, n):
    if a % n < 10:
        s = str(a % n)
    else:
        s = chr(a % n - 10 + ord('A'))
    if a // n != 0:
        s = str(to_sys(a//n, n)) + s
    return s


x, sys = [int(x) for x in input().split()]
if x < 0:
    y = '-' + to_sys(-x, sys)
else:
    y = to_sys(x, sys)
print(y)