def func(n, k):
    row1 = (k // n)
    row2 = ((k - n) // (n + 1))
    row = row1+(row1 - row2)
    seat = (k % n)-(row//2)
    if seat < 0:
        seat = n
        row -= 1
    if seat == 0:
        seat = 1 + n
        row -= 1
        if row2 == 0:
            seat -= n
            row += 1
    print(row, seat)


func(int(input()), int(input()))


