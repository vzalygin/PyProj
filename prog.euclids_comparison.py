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
        k = a // b
        n1 = (a - k * b)
        n2 = -(a - (k - 1) * b)
        if n1 < n2:
            a, b = b, n1
        else:
            a, b = b, n2
    return b


def measure(func, nums):
    w_time = 0
    s_time = time.time()
    for n in nums:
        func(n[0], n[0])
    e_time = time.time()
    w_time += e_time - s_time
    return w_time


funcs = [naive_euclids_algorithm, complete_euclids_algorithm]

print('Генерация списка чисел')
nums = [[random.randrange(100000000000000, 10000000000000000), random.randrange(100000000000000, 10000000000000000)] \
        for _ in range(1000000)]

print('Измерение времени работы')
times = []
for func in funcs:
    times.append(measure(func, nums))

print('Наивный алгоритм Евклида: {:0.15f}'.format(times[0]))
print('Стандартный алгоритм Евклида: {:0.15f}'.format(times[1]))
if times[0] < times[1]:
    print('Наивный алгоритм Евклида быстрее')
elif times[1] < times[0]:
    print('Стандартный алгоритм Евклида быстрее')
