import random


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


def psort_inplace(array, left=0, right=None):
    """Упорядочивает кусок array[left:right]"""
    if right is None: right = len(array)
    if right - left < 2: return
    pivot_index = partition_inplace(array, left, right)
    psort_inplace(array, left, pivot_index)
    psort_inplace(array, pivot_index + 1, right)


def partition_inplace(array, left, right):
    # pivot = array[random.randrange(left, right)]
    pivot_ind = left
    pivot = array[pivot_ind]
    # проход по массиву и анализ
    less = 0
    equal = 0
    great = 0
    for i in range(left, right):
        if array[i] > pivot:
            great += 1
        elif array[i] < pivot:
            less += 1
        else:
            equal += 1
    array[pivot_ind], array[less] = array[less], array[pivot_ind]
    pivot_ind = less
    for i in range(left, right):
        pass
    print(less, equal, great)
    return array.index(array[pivot_ind])


foo = [5, 3, 6, 2, 8, 9, 1, 4, 7, 5, 6, 5]
partition_inplace(foo, 0, len(foo))
print(foo)
# psort_inplace(foo)
