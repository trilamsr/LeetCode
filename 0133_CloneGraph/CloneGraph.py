"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# DFS
class Solution:
    def __init__(self):
        self.cache = {}
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node in self.cache: return self.cache[node]
        newNode = Node(node.val, [])
        self.cache[node] = newNode
        newNode.neighbors = [self.cloneGraph(n) for n in node.neighbors]
        return newNode

# BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        cache, queue = {node: Node(node.val, [])}, [node]
        while queue:
            cur = queue.pop()
            for n in cur.neighbors:
                if n not in cache:
                    queue.append(n)
                    cache[n] = Node(n.val, [])
                cache[cur].neighbors.append(cache[n])
        return cache[node]
