class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue , ret = collections.deque([root]), []
        left_to_right = True
        for level in self.get_by_level(queue):
            ret.append(level if left_to_right else level[::-1])
            left_to_right = not left_to_right
        return ret
        
    def get_by_level(self, queue):
        while queue:
            cur_level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                cur_level.append(node.val)
            yield cur_level