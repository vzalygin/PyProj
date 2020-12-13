t = input()
s = input()
n = int(input())
tmp = ''
t_l = len(t)
count = 0
for i in range(n):
    tmp += s
s = tmp
s_l = len(s)
for i in range(s_l):
    if s[i] == t[0]:
        n = 1
        for j in range(1, t_l):
            if i+j < s_l:
                if s[i+j] == t[j]: n += 1
            else: break
        if n == t_l:
            count += 1
print(count)
