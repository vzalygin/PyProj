a = [int(x) for x in input().split()]
x = int(input())
for i in range(len(a)):
    if a[i] < x:
        print(i+1)
        exit()
print(len(a)+1)
