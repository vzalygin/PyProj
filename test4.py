with open('ABC.txt', 'r') as f:
    s = [x for x in f.read().replace('A', 'B').replace('B', ' ').split(' ') if len(x) > 0]
    print(len(max(s)))

