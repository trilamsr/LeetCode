from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ret = defaultdict(list)
        def recurse(node, level):
            if not node: return
            ret[level].append(node.val)
            for child in node.children:
                recurse(child, level+1)
        recurse(root, 0)
        return ret.values()

# ---------------------------------

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        ret = []
        queue = deque([root])
        while queue:
            ret.append([])
            for i in range(len(queue)):
                cur = queue.popleft()
                ret[-1].append(cur.val)
                queue.extend(cur.children)
        return ret
