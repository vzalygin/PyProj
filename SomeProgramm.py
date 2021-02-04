def sumOfNum(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s


num = -1
max_sum = 0
max_num = 0
while num != 0:
    num = int(input())
    curr_sum = sumOfNum(num)
    if curr_sum > max_sum:
        max_sum = curr_sum
        max_num = num
print(f'{max_num} с суммой {max_sum}')
