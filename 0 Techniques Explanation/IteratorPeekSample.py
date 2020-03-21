class PeekIterator:
    
    def __init__(self, it):
        self.it = it
        self.slot = None
        self._advance()
        
    def __iter__(self):
        yield self.slot
        yield from self.it
        
    def __bool__(self):
        return self.hasNext()
    
    def __next__(self):
        if not self.hasNext():
            raise StopIteration
        ret = self.slot
        self._advance()
        return ret
        
    def peek(self):
        if not self.hasNext():
            raise Exception('empty')
        return self.slot
    
    def hasNext(self):
        return self.slot != None
    
    def _advance(self):
        try:
            self.slot = next(self.it)
        except:
            self.slot = None

        
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        A = PeekIterator(iter_inorder(root1))
        B = PeekIterator(iter_inorder(root2))
        result = []
        while A and B:
            if A.peek() < B.peek():
                result.append(next(A))
            else:
                result.append(next(B))
        result.extend(A or B)
        return result

def iter_inorder(node):
    while node:
        if not node.left:
            yield node.val
            node = node.right
        else:
            pred = predecessor(node)
            if not pred.right:
                pred.right, node = node, node.left
            else:
                yield node.val
                pred.right, node = None, node.right
        
        
def predecessor(node):
    ret = node.left
    while ret.right and ret.right != node:
        ret = ret.right
    return ret