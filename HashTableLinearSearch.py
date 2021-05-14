class Dict:
    def __init__(self, k=8):
        self.size = 0
        self.table = [None for _ in range(k)]

    def __len__(self):
        return self.size

    def __contains__(self, key):
        i = hash(key) % len(self.table)
        j = 0
        contains = False
        while self.table[i] is not None and j < len(self.table):
            if self.table[i][0] == key:
                contains = True
                break
            i = (i + 1) % len(self.table)
            j += 1
        return contains

    def __getitem__(self, key):
        i = hash(key) % len(self.table)
        j = 0
        while self.table[i] is not None and j < len(self.table):
            if self.table[i][0] == key:
                return self.table[i][1]
            i = (i + 1) % len(self.table)
            j += 1
        raise KeyError()

    def __setitem__(self, key, value):
        if self.size > len(self.table)//2:
            self.update_size(len(self.table)*2)
        i = hash(key) % len(self.table)
        while self.table[i] is not None:
            if self.table[i][0] == key:
                break
            i = (i + 1) % len(self.table)
        self.table[i] = (key, value)
        self.size += 1

    def __delitem__(self, key):
        i = hash(key) % len(self.table)
        j = 0
        while self.table[i] is not None and j < len(self.table):
            if self.table[i][0] != key:
                self.table[i] = None
                break
            i = (i + 1) % len(self.table)
            j += 1

    def __repr__(self):
        output = ''
        for pair in self.table:
            output += str(pair) + '\n'
        return output

    def update_size(self, k):
        new_table = [None for _ in range(k)]
        for pair in self.table:
            if pair is not None:
                i = hash(pair[0]) % len(new_table)
                while new_table[i] is not None:
                    i = (i + 1) % len(new_table)
                new_table[i] = (pair[0], pair[1])
        self.table = new_table

def check_data_structure(struct, a, b, count):
    from random import randint
    test = []
    for i in range(count):
        # Set
        key, num = randint(a, b), randint(a, b)
        
        # Get
        # Check
        # Del

import sys
exec(sys.stdin.read())


