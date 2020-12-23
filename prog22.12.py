import sys
a = [int(x) for x in sys.stdin.read().split() if int(x) >= 0]
a.sort()
n = 0
if len(a) == 1:
    n = a[0]+1
    if a[0] == 0:
        n = max(a) + 1
for i in range(len(a)-1):
    if abs(a[i]-a[i+1]) > 1:
        n = a[i]+1
        break
print(n)
