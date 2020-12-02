def func(n):
    if n % 1 != 0.0:
        return False
    if n == 1:
        return True    
    return func(n/2)


if func(int(input())):
    print('YES')
else:
    print('NO')
