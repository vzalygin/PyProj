a = int(input())
b = int(input())
btn = True
flag = True
count1 = 0
count2 = 0
big = False
if ((a + b) % 3) != 0:
    print(-1)
    flag = False
while flag:
    if a > 100 and b > 100:
        big = True
        a = a / 10
        b = b / 10
    if a > b or a == b and a != 0 and b != 0:
        a -= 2
        b -= 1
        count1 += 1
    elif a < b:
        a -= 1
        b -= 2
        count2 += 1
    elif a == 0 and b == 0:
        if big:
            print(count1 * 10, count2 * 10)
        else:
            print(count1, count2)
        flag = False
    if a < 0 or b < 0:
        print(-1)
        flag = False