from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        stack = deque([root])
        level = 0
        while stack:
            level +=1
            for i in range(len(stack)):
                cur = stack.popleft()
                if not cur.left and not cur.right: return level
                if cur.left: stack.append(cur.left)
                if cur.right: stack.append(cur.right)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque()
        if not root: return 0
        queue.append({'node':root, 'depth': 1})
        while len(queue) > 0:
            element = queue.popleft()
            if not element['node'].left and not element['node'].right: return element['depth']
            if element['node'].left:
                queue.append({'node': element['node'].left, 'depth': element['depth']+1})
            if element['node'].right:
                queue.append({'node': element['node'].right, 'depth': element['depth']+1})

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        ret = float('inf')
        if not root: return 0
        def recurse(node, depth):
            nonlocal ret
            if not node: return
            if not node.left and not node.right:
                ret = ret if ret < depth else depth
            recurse(node.left, depth+1)
            recurse(node.right, depth+1)
        recurse(root, 1)
        return ret

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0;
        if not root.left: return 1 + self.minDepth(root.right)
        if not root.right: return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


