a = [int(x) for x in input().split()]
k = int(input())

l = len(a)
ind = (l - k) % l
n = a[ind]

for _ in range(l):
    ind = (ind + k) % l
    next_n = a[ind]
    a[ind] = n
    n = next_n
print(*a)
