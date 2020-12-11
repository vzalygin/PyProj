def empty(): return None
def join(x, lst): return (x, lst)
def is_empty(lst): return lst == None
def head(lst): return lst[0]
def tail(lst): return lst[1]


def process(lst):
    N = list_length(lst)
    res = []
    for sorted_length in range(N):
        n, min_in = list_min(lst, sorted_length, 0)
        lst = set(lst, min_in, get(lst, sorted_length))
        lst = set(lst, sorted_length, n)
        res.append(lst)
    return res


def list_min(lst, s, i):
    if not is_empty(tail(lst)):
        min_n, j = list_min(tail(lst), s, i+1)
    else: return head(lst), i
    if i >= s and head(lst) <= min_n: return head(lst), i
    else: return min_n, j


def list_length(lst):
    l = 0
    while not is_empty(lst):
        lst = tail(lst)
        l += 1
    return l


def get(lst, i):
    n = 0
    while n != i:
        n += 1
        lst = tail(lst)
    return head(lst)


def set(lst, i, x):
    n = 0
    res = empty()
    while not is_empty(lst):
        if n == i: res = join(x, res)
        else: res = join(head(lst), res)
        n += 1
        lst = tail(lst)
    return reverse(res)


def reverse(lst):
    res = empty()
    while not is_empty(lst):
        res = join(head(lst), res)
        lst = tail(lst)
    return res


import sys
exec(sys.stdin.read())
