import time
import random


def merge(a, b):
    res = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr[:]
    left, right = merge_sort(arr[:n // 2]), merge_sort(arr[n // 2:])
    return merge(left, right)


def partition(arr):
    x = arr[0]
    less, equal, greater = [], [], []
    for y in arr:
        if y < x:
            less.append(y)
        elif y > x:
            greater.append(y)
        else:
            equal.append(y)
    return less, equal, greater


def partition_sort(arr):
    if len(arr) < 2: return arr[:]
    less, equal, greater = partition(arr)
    return partition_sort(less) + equal + partition_sort(greater)


def sort_comparison(N, k):
    m_sort_average_time = 0
    p_sort_average_time = 0
    for _ in range(k):
        a = []
        for __ in range(N):  # Генерация массива с длинной N
            a.append(random.randrange(0, 1000000000))
        s_time = time.time()
        merge_sort(a[:])
        e_time = time.time()
        a_time = e_time - s_time
        m_sort_average_time += a_time

        s_time = time.time()
        partition_sort(a[:])
        e_time = time.time()
        a_time = e_time - s_time
        p_sort_average_time += a_time
    m_sort_average_time /= k
    p_sort_average_time /= k
    return m_sort_average_time, p_sort_average_time


for i in range(0, 7):
    m_sort, p_sort = sort_comparison(10 ** i, 5)
    if m_sort < p_sort:
        print('m_sort is {:0.15f} sec. faster than p_sort on {:d} array elements' \
              .format(float(p_sort) - float(m_sort), 10 ** i))
    elif m_sort > p_sort:
        print('p_sort is {:0.15f} sec. faster than m_sort on {:d} array elements' \
              .format(float(m_sort) - float(p_sort), 10 ** i))
    else:
        print('working time is too short on {:d} array elements'.format(10 ** i))
    print('{:0.15f} {:0.15f}'.format(m_sort, p_sort))
