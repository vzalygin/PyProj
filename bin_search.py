import sys


def search(func, needle, arr, n, bound):
    a = 0
    b = len(arr)
    while a != b:
        m = (a + b) // 2
        if m < 0 or m > len(arr):
            if bound == 0: return 0
            else: return len(arr)
        if func(arr[m], n, bound) == needle:
            b = m
        else:
            a = m + 1
    return a


def func(el, n, bound):
    if bound == 0: # больше указанного
        return el >= n
    elif bound == 1: # меньше указанного
        return not el < n


inp = [int(x) for x in sys.stdin.read().split()]
n = inp[0]
arr = inp[1:-2]
a, b = inp[-2], inp[-1]
try:
    l = search(func, True, arr, a, 0)
    u = search(func, True, arr, b, 1)
    print(*arr[l:u])
except:
    print()