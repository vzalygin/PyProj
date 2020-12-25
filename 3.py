x = 16
a = [3, 8, 11, 15, 25, 33, 42, 64, 74, 75, 86, 87, 91, 95, 99]
left = 0
right = 14
while right - left > 1:
    m = (right + left) // 2
    if a[m] < x:
        left = m
    else:
        right = m
print(left, right)