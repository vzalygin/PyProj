p = int(input())
g = int(input())
c = int(input())
if g / ((g+p)//c+1) >= 2:
    print((g+p)//c+1)
else:
    print(0)
