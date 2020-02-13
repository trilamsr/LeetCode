# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(S*T)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t: return True
        if not s or not t: return False
        return self.same_tree(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def same_tree(self, s, t):
        if not s and not t: return True
        if not s or not t: return False
        return s.val == t.val and self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right)


# M_BRAX's SOLUTION
O(S+T+S)
def kmp(text, pattern):
    print(text)
    print(pattern)
    if len(text) < len(pattern): 
        return False
    if len(pattern) == 0: 
        return len(text) == 0
    
    n = len(pattern)
    fnodes = [0] * n
    for i in range(1, n):
        j = fnodes[i-1]
        while j and pattern[i] != pattern[j]:
            j = fnodes[j-1]
        j += pattern[i] == pattern[j]
        fnodes[i] = j
    node = 0
    for i in range(len(text)):
        while node and pattern[node] != text[i]:
            node = fnodes[node-1]
        node += pattern[node] == text[i]
        if node == len(pattern):
            return True
    return False

def build_prefix_repr(node):
    result = []
    def dfs(node):
        if not node:
            result.append('_')
            return
        result.append('$' + str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(node)
    return ''.join(result)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        str_s = build_prefix_repr(s)
        str_t = build_prefix_repr(t)
        return kmp(str_s, str_t)
        # return str_t in str_s

