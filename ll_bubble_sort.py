def empty(): return None
def join(x, lst): return (x, lst)
def is_empty(lst): return lst == None
def head(lst): return lst[0]
def tail(lst): return lst[1]


def print_list(lst):
    while not is_empty(lst):
        print(head(lst), end=' ')
        lst = tail(lst)


def list_length(lst):
    result = 0
    while not is_empty(lst):
        lst = tail(lst)
        result += 1
    return result


def ll_b_sort(lst):
    length = list_length(lst)
    for _ in range(length-1):
        lst = ll_permutation(lst)
    return lst


def ll_permutation(lst):
    if not is_empty(tail(lst)):
        if head(lst) > head(tail(lst)):
            tmp = head(lst)
            lst = join(head(tail(lst)), join(tmp, tail(tail(lst))))
            lst = join(head(lst), ll_permutation(tail(lst)))
    return lst


def main():
    lst = join(5, join(4, join(3, join(2, join(1, empty())))))
    lst = ll_b_sort(lst)
    print_list(lst)


main()
