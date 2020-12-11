a = [int(x) for x in input().split()]
for i in range(len(a)//2):
    a[i], a[-i-1] = a[-i-1], a[i]
print(*a)

