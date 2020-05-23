class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2: return True
        rank = {v:i for i, v in enumerate(order)}
        keys = list([self.key(word, rank) for word in words])
        for i, key in enumerate(keys):
            if i == 0: continue
            if key < keys[i-1]: return False
        return True
        
    def key(self, word, rank):
        return tuple((rank[char] for char in word))

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) < 2: return True
        dictionary = dict(zip(order, list(range(26))))
        for i in range(1, len(words)):
            a, b = words[i-1], words[i]
            if not self.is_sorted(a, b, dictionary):
                return False
        return True
    
    def is_sorted(self, a, b, dictionary):
        i, j = 0, 0
        for ind in range(max(len(a), len(b))):
            if ind < len(a): i += dictionary[a[ind]]
            if ind < len(b): j += dictionary[b[ind]]
            if i > j: return False
            if i < j: return True
        return i <= j