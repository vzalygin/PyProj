def rapid_exponentiation(x, n):
    if n % 2 == 0:
        x **= 2
        x **= n/2
    else:
        x *= x**(n-1)
    return x


print(rapid_exponentiation(float(input()), float(input())))
