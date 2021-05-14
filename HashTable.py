class Dict:
    def __init__(self, k=8):
        self.size = 0
        self.table = [[] for _ in range(k)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        pairs = self.table[hash(key) % len(self.table)]
        for i in range(len(pairs)):
            if pairs[i][0] == key:
                return True
        return False

    def __getitem__(self, key):
        pairs = self.table[hash(key) % len(self.table)]
        for i in range(len(pairs)):
            if pairs[i][0] == key:
                return pairs[i][1]
        raise KeyError()

    def update_size(self, k):
        new_table = [[] for _ in range(k)]
        for pairs in self.table:
            for pair in pairs:
                new_table[hash(pair[0]) % len(new_table)].append((pair[0], pair[1]))
        self.table = new_table

    def __setitem__(self, key, value):
        if self.size > len(self.table)//2:
            self.update_size(len(self.table)*2)
        pairs = self.table[hash(key) % len(self.table)]
        for i in range(len(pairs)):
            if pairs[i][0] == key:
                pairs[i] = (key, value)
                return
        pairs.append((key, value))
        self.size += 1

    def __delitem__(self, key):
        pairs = self.table[hash(key) % len(self.table)]
        for i in range(len(pairs)):
            if pairs[i][0] == key:
                pairs.pop(i)
                self.size -= 1
                return

    def __repr__(self):
        output = ''
        for pairs in self.table:
            output += str(pairs) + '\n'
        return output

import sys
exec(sys.stdin.read())

