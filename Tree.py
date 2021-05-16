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

    def __len__(self):
        if not self.is_empty(self.root):
            return len(self.root)
        else:
            return 0

    def __repr__(self):
        return str(self.root)

    def is_empty(self, tree):
        return tree is None

    def set(self, tree, key, value):
        if self.is_empty(tree):
            return Node(key, value)
        elif tree.key== key:
            return Node(key, value, node=tree)
        elif key < tree.key:
            new_tree = Node(left=self.set(tree.left, key, value), node=tree)
        else:
            new_tree = Node(right=self.set(tree.right, key, value), node=tree)

        if abs(new_tree.right_height - new_tree.left_height) > 1:
            return self.rotation(new_tree)
        return new_tree

    def rotation(self, tree):
        if tree.right_height - tree.left_height > 0: # левое вращение
            return Node(tree.right.key, tree.right.value, Node(tree.key, tree.value, tree.left, tree.right.left), tree.right.right)
        else:
            return Node(tree.left.key, tree.left.value, tree.left.left, Node(tree.key, tree.value, tree.left.right, tree.right))

    def get(self, tree, key):
        if self.is_empty(tree):
            raise KeyError()
        elif key == tree.key:
            return tree.value
        elif key < tree.key:
            return self.get(tree.left, key)
        else:
            return self.get(tree.right, key)

    def find_for_delete(self, tree):
        if self.is_empty(tree.right):
            return tree.key, tree.value, tree.left
        key, value, right_tree = self.find_for_delete(tree.right)
        return key, value, Node(tree.key, tree.value, tree.left, right_tree)

    def delete(self, tree, key):
        if self.is_empty(tree): return None
        if key == tree.key:
            if not self.is_empty(tree.left):
                key2, value, left_tree = self.find_for_delete(tree.left)
                return Node(key2, value, left_tree, tree.right)
            elif not self.is_empty(tree.right):
                return tree.right
            else:
                return None
        if key < tree.key:
            return Node(tree.key, tree.value, self.delete(tree.left, key), tree.right)
        else:
            return Node(tree.key, tree.value, tree.left, self.delete(tree.right, key))


class Node:
    def __init__(self, key=None, value=None, left=None, right=None, node=None):
        #filling data
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.length = 1
        if node is not None:
            if self.key is None: self.key = node.key
            if self.value is None: self.value = node.value
            if self.left is None: self.left = node.left
            if self.right is None: self.right = node.right

        #length
        if self.right is not None:
            self.length += self.right.length
        if self.left is not None:
            self.length += self.left.length

        #height
        self.left_height = 0
        self.right_height = 0
        if self.left is not None: self.left_height = self.left.height + 1
        if self.right is not None: self.right_height = self.right.height + 1
        self.height = max(self.left_height, self.right_height)

    def __repr__(self):
        return '(l=' + str(self.length) + ' h=' + str(self.height) + ' ' + str(self.key) + '=' + str(self.value) + ', left=' + str(self.left) + ', right=' + str(self.right) + ')'

    def __len__(self):
        return self.length

import sys
exec(sys.stdin.read())
