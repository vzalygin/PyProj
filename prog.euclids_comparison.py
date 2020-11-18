import time
import random


def naive_euclids_algorithm(a, b):
    if b > a:
        a, b = b, a
    while a % b > 0:
        a, b = b, a % b
    return b


def complete_euclids_algorithm(a, b):
    if b > a:
        a, b = b, a
    while a % b > 0:
        k = -(a//b)
        if (a + k*b) < -(a + (k-1)*b):
            a, b = b, a + k*b
        else:
            a, b = b, -(a + (k-1)*b)
    return b


def measure(func, nums):
    w_time = 0
    for n in nums:
        s_time = time.time()
        func(n[0], n[0])
        e_time = time.time()
        w_time += e_time - s_time
    w_time /= len(nums)
    return w_time


funcs = [naive_euclids_algorithm, complete_euclids_algorithm]
nums = [[random.randrange(1, 1000000000000), random.randrange(1, 1000000000000)] for _ in range(1000)]
for n in nums:
    times = []
    for func in funcs:
        s_time = time.mktime(time.strptime(time.asctime()))
        func(n[0], n[0])
        e_time = time.mktime(time.strptime(time.asctime()))
        times.append(e_time - s_time)
    print('Числа: {:d} {:d}'.format(n[0], n[1]))
    print('Наивный алгоритм Евклида: {:0.15f}'.format(times[0]))
    print('Стандартный алгоритм Евклида: {:0.15f}'.format(times[1]))
    if times[0] > times[1]:
        print('Наивный алгоритм Евклида быстрее')
    elif times[1] > times[0]:
        print('Стандартный алгоритм Евклида быстрее')
