def empty(): return None
def join(x, lst): return (x, lst)
def is_empty(lst): return lst == None
def head(lst): return lst[0]
def tail(lst): return lst[1]


def list_length(lst):
    l = 0
    while not is_empty(lst):
        lst = tail(lst)
        l += 1
    return l


def process(lst):
    result = []
    N = list_length(lst)
    for sorted_length in range(N):
        lst = func(lst, sorted_length, 0)
        result.append(lst)
    return result


def func(lst, sorted_length, i):
    if i < sorted_length:
        lst = join(head(lst), func(tail(lst), sorted_length, i + 1))
    else:
        return lst
    if head(lst) > head(tail(lst)):
        lst = join(head(tail(lst)), join(head(lst), tail(tail(lst))))
    return lst


import sys
exec(sys.stdin.read())
