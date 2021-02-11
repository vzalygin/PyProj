ch = input()
ch_count = int(input())
x = ch_count-1
for __ in range(ch_count):
    space_count = ch_count - 1 + x
    for i in range(ch_count):
        s = ''
        for _ in range(space_count):
            s = s + ' '
        space_count -= 1
        for _ in range(i * 2 + 1):
            s = s + ch
        print(s)
    ch_count = ch_count + 1
    x = x - 1
