class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        mem = collections.defaultdict(int)
        for char in s:
            mem[char] += 1
        for i in range(len(s)):
            if mem[s[i]] == 1: return i  
        return -1
    

class Solution:
    def firstUniqChar(self, s: str) -> int:
        index=[s.index(letter) for letter in string.ascii_lowercase if s.count(letter) == 1]
        return min(index) if len(index) > 0 else -1


# M_BRAX's Solution - 1 pass

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        
class LinkedHashQueue:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
    def append(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.size += 1
        
    # PEEK LEFT
    def popleft(self):
        assert self.size
        return self.head.next
        

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return -1
        
        count = collections.defaultdict(int)
        queue = LinkedHashQueue()
        char_to_node = {}
        
        for index, ch in enumerate(s):
            # inserting for the first time
            if count[ch] == 0:
                node = Node(index)
                char_to_node[ch] = node
                queue.append(node)
                count[ch] += 1
                
            # seen for the second time so remove the element
            elif count[ch] == 1:
                queue.remove(char_to_node[ch])
                del char_to_node[ch]
                count[ch] += 1
                
            # if we have seen it more than twice: it implies we removed
            # so we do nothing
        
        return queue.popleft().val if len(queue) else -1