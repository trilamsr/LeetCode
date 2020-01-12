"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        queue = collections.deque([root])
        while queue:
            leng = len(queue)
            for i in range(leng):
                cur = queue.popleft()
                if cur.left and cur.right: 
                    queue.append(cur.left)
                    queue.append(cur.right)
                cur.next = queue[0] if i != leng-1 else None
        return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return None
        self.recurse(root.left, root.right)
        return root
    
    def recurse(self, left, right):
        if left: 
            left.next = right
        if left and left.left:
            left.right.next = right.left
            self.recurse(left.left, left.right)
            self.recurse(left.right, right.left)
            self.recurse(right.left, right.right)

# m_brax

class Solution:
    def connect(self, root: "Node") -> "Node":
        if not root:
            return None
        curr = root
        while curr:
            connect_below_pointers(curr)
            curr = next_level(curr)
        return root

def connect_below_pointers(node):
    while node:
        can_connect_left_child = node.left != None
        can_connect_right_child = node.right != None and node.next != None
        if can_connect_left_child:
            node.left.next = node.right
        if can_connect_right_child:
            node.right.next = node.next.left
        node = node.next

def next_level(node):
    return node.left
