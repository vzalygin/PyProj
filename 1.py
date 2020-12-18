def empty(): return None
def join(x, lst): return (x, lst)
def is_empty(lst): return lst == None
def head(lst): return lst[0]
def tail(lst): return lst[1]


def process(sublst, lst):
    while not is_empty(lst):
        if head(lst) == head(sublst):
            sublst_tmp = tail(sublst)
            lst_tmp = tail(lst)
            while not is_empty(sublst_tmp) and not is_empty(lst_tmp):
                if head(sublst_tmp) != head(lst_tmp):
                    break
            if not is_empty(sublst_tmp):
                pass
            else: return True
        lst = tail(lst)
        sublst = tail(sublst)
    return False


import sys
exec(sys.stdin.read())