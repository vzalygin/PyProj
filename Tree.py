class Dict:
    def __init__(self):
        self.root = None

    def __getitem__(self, key):
        return self.get(self.root, key)

    def __contains__(self, key):
        try:
            self.get(self.root, key)
            successful = True
        except:
            successful = False
        return successful

    def __setitem__(self, key, value):
        self.root = self.set(self.root, key, value)

    def __delitem__(self, key):
        self.root = self.delete(self.root, key)

    def __repr__(self):
        return str(self.root)

    def __len__(self):
        if not self.is_empty(self.root):
            return self.root[4]
        else:
            return 0

    def is_empty(self, tree):
        return tree is None

    def get_sum(self, tree):
        res = 0
        if tree[1] is not None:
            res += tree[1][4]
        if tree[2] is not None:
            res += tree[1][4]
        res += 1
        print(tree, res)
        return res

    def get_height(self, tree):
        res = 0
        if tree[1] is not None:
            if res < tree[1][3]:
                res = tree[1][3]
        if tree[2] is not None:
            if res < tree[2][3]:
                res = tree[2][3]
        res += 1
        return res

    def set(self, tree, key, value):
        if self.is_empty(tree):
            return ((key, value), None, None, 1, 1)
        elif tree[0][0] == key:
            return ((key, value), tree[1], tree[2], tree[3], tree[4])
        elif key < tree[0][0]:
            tree_tmp = (tree[0], self.set(tree[1], key, value), tree[2], 0, 0)
            return (tree[0], tree_tmp[1], self.get_height(tree_tmp), self.get_sum(tree_tmp))
        else:
            tree_tmp = (tree[0], tree[1], self.set(tree[2], key, value), 0, 0)
            return (tree[0], tree[1], tree_tmp[2], self.get_height(tree_tmp), self.get_sum(tree_tmp))

    def get(self, tree, key):
        if self.is_empty(tree):
            raise KeyError()
        elif key == tree[0][0]:
            return tree[0][1]
        elif key < tree[0][0]:
            return self.get(tree[1], key)
        else:
            return self.get(tree[2], key)

    def find_for_delete(self, tree):
        if self.is_empty(tree[2]):
            return tree[0], tree[1]
        el, left_tree = self.find_for_delete(tree[2])
        return el, (tree[0], tree[1], left_tree)

    def delete(self, tree, key):
        if self.is_empty(tree): return None
        if key == tree[0][0]:
            if not self.is_empty(tree[1]):
                el, left_tree = self.find_for_delete(tree[1])
                return (el, left_tree, tree[2])
            elif not self.is_empty(tree[2]):
                return tree[2]
            else:
                return None
        if key < tree[0][0]:
            return (tree[0], self.delete(tree[1], key), tree[2], tree[3], tree[4])
        else:
            return (tree[0], tree[1], self.delete(tree[2], key), tree[3], tree[4])

tree = Dict()
tree[5] = 1
tree[4] = 2
tree[6] = 3
tree[7] = 4
print(tree)

import sys
exec(sys.stdin.read())
