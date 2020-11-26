import random


def permutations(elements):
    if len(elements) == 0: return [[]]

    return [
        [elements[i]] + p
        for i in range(len(elements))
        for p in permutations(elements[:i] + elements[i + 1:])
    ]


def psort_inplace(array, left=0, right=None):
    """Упорядочивает кусок array[left:right]"""
    if right == None:
        right = len(array)

    if right - left < 2: return

    pivot_index = partition_inplace(array, left, right)

    psort_inplace(array, left, pivot_index)
    psort_inplace(array, pivot_index + 1, right)


def partition_inplace(array, left, right):
    """Разбиение массива на элементы меньше и больше pivot. Нельзя дополнительные массивы"""
    pivot = array[random.randrange(left, right)]
    # TODO Разбиение
    return array.index(pivot)


foo = [1, 2, 3]
psort_inplace(foo)

# ДОМАШНЕЕ ЗАДАНИЕ: реализовать partition_inplace
# должен за O(1) памяти:
# * выбирать опорный элемент случайным образом
# * располагать элементы в порядке: меньше опорного, равные опорному, больше опорного
# * возвращать какой-нибудь из индексов элементов, равных опорному
