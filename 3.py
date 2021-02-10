start = int(input())
end = int(input())
step = int(input())
k = int(input()) % 10
while start <= end:
    if start % 10 == k:
        break
    print(start, end=' ')
    start += step
