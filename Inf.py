el = [0]


def phib(n):
    if len(el) < n:
        phib(n-1)
    elif n == 1:
        el.append(1)
        return
    el.append(el[n-1] + el[n-2])


phib(int(input()))
print(el[-1])
