# from igraph import Graph, plot, layout

class Node:

    def __init__(self, value):
        self.count = 1
        self.height = 1
        self.min = value
        self.max = value
        self.total = value
        self.val = value
        self.left = None
        self.right = None

    def pull(self):
        # reset
        print(f'    | {self.val}.pull()')
        self.count = 1
        self.height = 0
        self.total = self.val
        self.min = self.val
        self.max = self.val

        if self.left:
            print(f'        pulling from [LEFT] ... {self.left.val}')
            self.count += self.left.count
            self.height = max(self.height, self.left.height)
            self.min = min(self.min, self.left.min)
            self.max = max(self.max, self.left.max)
            self.total += self.left.val

        if self.right:
            print(f'        pulling from [RIGHT] ... {self.right.val}')
            self.count += self.right.count
            self.height = max(self.height, self.right.height)
            self.min = min(self.min, self.right.min)
            self.max = max(self.max, self.right.max)
            self.total += self.right.val

        self.height += 1


class BST:

    def __init__(self):
        self.root = None

    def __len__(self):
        return self.root.count if self.root else 0

    def height(self):
        return self.root.height

    def add(self, val):
        print(f'XXXX Adding {val}')
        self.root = self._insert(self.root, val)

    def max(self):
        return self.root.max

    def min(self):
        return self.root.min

    def total(self):
        return self.root.total

    def _insert(self, root, val):
        if not root:
            return Node(val)
        if val < root.val:
            root.left = self._insert(root.left, val)
        elif val > root.val:
            root.right = self._insert(root.right, val)
        root.pull()
        return root


import random

tree = BST()
lst = []
for i in range(5):
    val = random.randint(1, 1000)
    lst.append(val)
    tree.add(val)

print('XXXX length of tree:', len(tree))
print('XXXX total sum of tree:', tree.total())
print('XXXX height of tree:', tree.height())
print('XXXX min of tree:', tree.min())
print('XXXX max of tree:', tree.max())

print('XXXX All the elements added:', sorted(lst))
