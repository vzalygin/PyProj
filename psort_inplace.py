import random
import sys


def permutations(elements):
    if len(elements) == 0: return [[]]
    return [
        [elements[i]] + p
        for i in range(len(elements))
        for p in permutations(elements[:i] + elements[i + 1:])
    ]


def partition(numbers):
    pivot = numbers[random.randrange(len(numbers))]
    return (
        [x for x in numbers if x < pivot],
        [x for x in numbers if x == pivot],
        [x for x in numbers if x > pivot]
    )


def psort(numbers):
    if len(numbers) <= 1: return numbers[:]
    left, mid, right = partition(numbers)
    return psort(left) + mid + psort(right)


def p(array, a, b):
    array[a], array[b] = array[b], array[a]


def psort_inplace(array, left=0, right=None):
    """Упорядочивает кусок array[left:right]"""
    if right is None: right = len(array)
    if right - left < 2: return
    pivot_index_s, pivot_index_e = partition_inplace(array, left, right)
    psort_inplace(array, left, pivot_index_s)
    psort_inplace(array, pivot_index_e, right)


def partition_inplace(array, left, right):
    pivot_ind = random.randrange(left, right)
    pivot = array[pivot_ind]
    p(array, left, pivot_ind)
    pivot_ind = left

    for i in range(left + 1, right):  # перекидываем все элементы меньще опорного на левую сторону
        if array[i] < pivot:
            p(array, pivot_ind, i)
            pivot_ind += 1
            p(array, pivot_ind, i)

    pivot_ind_e = pivot_ind + 1  # ставим элементы равные опорному рядом с ним
    for i in range(pivot_ind+1, right):
        if array[i] == pivot:
            p(array, pivot_ind_e, i)
            pivot_ind_e += 1
    return pivot_ind, pivot_ind_e


foo = [6, 9, 4, 2, 1, 7, 5, 3, 2, 8, 0, 0]
psort_inplace(foo)
print(*foo)
