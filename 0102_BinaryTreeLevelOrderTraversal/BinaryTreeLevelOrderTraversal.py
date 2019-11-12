from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = deque()
        queue.append(root)
        ret = []
        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                ele = queue.popleft()
                level.append(ele.val)
                if ele.left: queue.append(ele.left)
                if ele.right: queue.append(ele.right)
            ret.append(level)
        return ret



# ------------------------------
def adjacent(node):
    if node.left: yield node.left
    if node.right: yield node.right
    
def dfs(table, root, level):
    table[level].append(root.val)
    for child in adjacent(root):
        dfs(table, child, level + 1)
        
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        table = defaultdict(list)
        dfs(table, root, 0)
        return table.values()