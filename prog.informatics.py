import sys
import math


def func(a, div):
    s_a = math.sqrt(a)
    if a % div == 0:
        return False
    if s_a > div+1:
        return func(a, div+1)
    return True


sys.setrecursionlimit(1000000000)
n = int(input())
if n != 2:
    if func(n, 2):
        print('YES')
    else:
        print('NO')
else:
    print('YES')
