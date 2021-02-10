def empty(): return None
def join(x, lst): return (x, lst)
def is_empty(lst): return lst == None
def head(lst): return lst[0]
def tail(lst): return lst[1]


def to_ll(arr):
    res = empty()
    for i in range(len(arr)-1, -1, -1):
        res = join(arr[i], res)
    return res


def reverse(lst):
    res = empty()
    while not is_empty(lst):
        res = join(head(lst), res)
        lst = tail(lst)
    return res


def process(lst):
    sum_n = 0
    res = empty()
    while not is_empty(lst):
        res = join(sum_n, res)
        sum_n += head(lst)
        lst = tail(lst)
    return reverse(res)


# lst = to_ll([1, 0, 1, 0, 1])
# print(process(lst))
import sys
exec(sys.stdin.read())